"""Django-backed screens for the Linktag workspace."""
import csv
import io

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.http import require_POST

from apps.seeker.forms import (
    AddSeekerCSVContactInformationForm, SeekerCsvUploadForm, SeekerLoginForm,
    SeekerRegistrationForm, SeekerTargetRolesTagsForm,
)
from apps.seeker.models import Csv


def dashboard_context(request, contact=None, form=None, editing=False):
    """Every contact lookup starts from the authenticated owner's queryset."""
    contacts = Csv.objects.filter(seeker=request.user)
    tags = request.session.get('matched_tags', [])[:5]
    query = Q()
    for tag in tags:
        query |= Q(position__icontains=tag)
    matches = contacts.filter(query).order_by('first_name', 'last_name', 'id') if tags else contacts.none()
    entries = list(matches[:50])
    contact_id = request.GET.get('edit') or request.GET.get('contact')
    if contact is None and contact_id:
        if not contact_id.isdecimal():
            raise Http404
        contact = get_object_or_404(contacts, pk=contact_id)
    if contact is None:
        contact = entries[0] if entries else None
    if form is None:
        initial = {name: getattr(contact, name) for name in AddSeekerCSVContactInformationForm.base_fields} if contact else {}
        form = AddSeekerCSVContactInformationForm(initial=initial)
    return {
        'seeker': request.user, 'cv_entries': entries, 'matched_tags': tags,
        'selected_contact': contact, 'contact_form': form,
        'editing': editing or bool(request.GET.get('edit')),
        'contact_count': contacts.count(), 'match_count': matches.count(),
        'combined_q_objects': query, 'active_page': 'dashboard',
    }


@method_decorator(login_required, name='dispatch')
class SeekerDashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html', dashboard_context(request))


class SeekerRegistrationView(View):
    def get(self, request):
        return render(request, 'registration.html', {'registration_form': SeekerRegistrationForm()})

    def post(self, request):
        form = SeekerRegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    seeker = form.save()
                login(request, seeker, backend='django.contrib.auth.backends.ModelBackend')
                messages.success(request, 'Your account is ready. Bring your network into focus.')
                return redirect('seeker_csv_upload')
            except IntegrityError:
                form.add_error('email', 'This email is already in use. Please sign in.')
        return render(request, 'registration.html', {'registration_form': form})


class SeekerLoginView(View):
    def get(self, request):
        return render(request, 'login.html', {'login_form': SeekerLoginForm()})

    def post(self, request):
        form = SeekerLoginForm(request.POST)
        if form.is_valid():
            seeker = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if seeker is not None:
                login(request, seeker)
                messages.success(request, 'Signed in successfully.')
                return redirect('seeker_dashboard')
            form.add_error(None, 'Email or password is incorrect. Please try again.')
        return render(request, 'login.html', {'login_form': form})


class SeekerLogoutView(View):
    def post(self, request):
        logout(request)
        messages.success(request, 'You have been signed out.')
        return redirect('seeker_login')


def read_connections(upload):
    """Accept LinkedIn headers (with or without its export preamble), atomically."""
    if not upload.name.lower().endswith('.csv'):
        raise ValueError('Choose a CSV file exported from LinkedIn.')
    if upload.size > 5 * 1024 * 1024:
        raise ValueError('Choose a CSV smaller than 5 MB.')
    try:
        rows = csv.reader(io.StringIO(upload.read().decode('utf-8-sig')), strict=True)
        required = {'first name', 'last name', 'company', 'position'}
        headers = None
        result = []
        for line, row in enumerate(rows, 1):
            if not any(cell.strip() for cell in row):
                continue
            if headers is None:
                candidate = [cell.strip().lower().replace('_', ' ') for cell in row]
                if required.issubset(candidate):
                    headers = candidate
                elif line >= 20:
                    break
                continue
            if len(row) != len(headers):
                raise ValueError(f'Row {line} has missing or extra columns. Please check your CSV.')
            record = dict(zip(headers, (cell.strip() for cell in row)))
            values = {field: record[field.replace('_', ' ')] for field in ('first_name', 'last_name', 'company', 'position')}
            values['email'] = record.get('email address', record.get('email', ''))
            if any(len(value) > 255 for value in values.values()):
                raise ValueError(f'Row {line} contains a field longer than 255 characters.')
            if not values['first_name'] and not values['last_name']:
                continue
            result.append({key: value.lower() for key, value in values.items()})
            if len(result) > 10000:
                raise ValueError('Upload no more than 10,000 connections at a time.')
        if headers is None:
            raise ValueError('CSV must include First Name, Last Name, Company, and Position columns.')
        if not result:
            raise ValueError('This CSV has no connections to import.')
        return result
    except (UnicodeDecodeError, csv.Error) as error:
        raise ValueError('This file could not be read. Choose a UTF-8 LinkedIn CSV export.') from error


@method_decorator(login_required, name='dispatch')
class SeekerCsvUploadView(View):
    def get(self, request):
        return render(request, 'csv_upload.html', {'csv_form': SeekerCsvUploadForm(), 'active_page': 'upload'})

    def post(self, request):
        form = SeekerCsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                records = read_connections(form.cleaned_data['csv_file'])
            except ValueError as error:
                form.add_error('csv_file', str(error))
            else:
                with transaction.atomic():
                    for record in records:
                        email = record.pop('email')
                        # Preserve contact notes and previously added email on a re-import.
                        existing = Csv.objects.filter(seeker=request.user, **record).order_by('id').first()
                        if existing is None:
                            Csv.objects.create(seeker=request.user, email=email, **record)
                        elif email:
                            existing.email = email
                            existing.save(update_fields=['email'])
                messages.success(request, f'Imported {len(records)} connections. Choose your role tags next.')
                return redirect('seeker_roles_tags')
        return render(request, 'csv_upload.html', {'csv_form': form, 'active_page': 'upload'})


@method_decorator(login_required, name='dispatch')
class SeekerTargetRolesTagsView(View):
    def get(self, request, search_query=None):
        return self.render_form(request, SeekerTargetRolesTagsForm())

    def render_form(self, request, form):
        return render(request, 'rolestags.html', {
            'roles_tags_form': form, 'matched_tags': request.session.get('matched_tags', []),
            'active_page': 'tags',
        })

    def post(self, request, search_query=None):
        tags = request.session.get('matched_tags', [])[:5]
        if 'remove' in request.POST:
            request.session['matched_tags'] = [tag for tag in tags if tag != request.POST['remove']]
            return redirect('seeker_roles_tags')
        form = SeekerTargetRolesTagsForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data['search_query'].strip()
            if value.casefold() in [tag.casefold() for tag in tags]:
                form.add_error('search_query', 'That tag is already selected.')
            elif len(tags) >= 5:
                form.add_error('search_query', 'You can choose up to five tags. Remove one to add another.')
            else:
                # Keep user-selected roles even with zero matches; the dashboard explains the empty state.
                request.session['matched_tags'] = [*tags, value]
                return redirect('seeker_roles_tags')
        return self.render_form(request, form)


@login_required
@require_POST
def clear_tags(request):
    request.session.pop('matched_tags', None)
    return redirect('seeker_roles_tags')


@method_decorator(login_required, name='dispatch')
class AddSeekerCSVContactInformationView(View):
    def post(self, request, cv_entry_id):
        contact = get_object_or_404(Csv, pk=cv_entry_id, seeker=request.user)
        form = AddSeekerCSVContactInformationForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                setattr(contact, name, value)
            contact.save()
            messages.success(request, 'Contact details saved.')
            return redirect(f"{reverse('seeker_dashboard')}?contact={contact.pk}")
        return render(request, 'dashboard.html', dashboard_context(request, contact=contact, form=form, editing=True))
