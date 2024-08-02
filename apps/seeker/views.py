import csv

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import FormView
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.db import IntegrityError
from django.db.models import Q

from apps.seeker.forms import (
    SeekerRegistrationForm, 
    SeekerLoginForm, 
    SeekerCsvUploadForm, 
    SeekerTargetRolesTagsForm, 
    AddSeekerCSVContactInformationForm
)
from apps.seeker.models import Seeker, Csv


@method_decorator(login_required, name='dispatch')
class SeekerDashboardView(View):
    def get(self, request):
        # get the currently lodded-in user 
        user = request.user
        
        # check if the user is authenticated 
        if not user.is_authenticated:
            pass
        
        seeker_email = request.user.email
        matched_tags = request.session.get('matched_tags', [])
        form = AddSeekerCSVContactInformationForm()
        # Get the contact ID from query parameter
        edit_contact_id = request.GET.get('edit')
        
        # Create a list of Q objects for each matched tag
        q_objects = [Q(position__icontains=tag) for tag in matched_tags]
        
        # Combine the Q objects using OR operator
        combined_q_objects = Q()
        for q_object in q_objects:
            combined_q_objects |= q_object
        
        # Fetch the CV entries that match any of the tags
        cv_entries = Csv.objects.filter(combined_q_objects)[:10]
        
        if edit_contact_id:
            contact = get_object_or_404(Csv, id=edit_contact_id)
            initial_data = {
                'first_name': contact.first_name,
                'last_name': contact.last_name,
                'email': contact.email,
                'phone_number': contact.phone_number,
                'company': contact.company,
                'position': contact.position,
                'mini_bio': contact.mini_bio,
                'notes': contact.notes,
            }
            form = AddSeekerCSVContactInformationForm(initial=initial_data)
        
        context = {
            'seeker': request.user,
            'cv_entries': cv_entries,
            'contact_form': form,
            'combined_q_objects': combined_q_objects,
        }
        
        messages.success(request, f'Welcome {seeker_email} to your dashboard 🥂 👋')
        return render(request, 'dashboard.html', context)
    

#TODO Add loading screen to account registration for Req and Res cycle when we go live on heroku
class SeekerRegistrationView(View):
    def get(self, request):
        form = SeekerRegistrationForm()
        context = {
            'registration_form': form
        }
        
        return render(request, 'registration.html', context)
    
    def post(self, request):
        form = SeekerRegistrationForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            
            if Seeker.objects.filter(email=email).exists():
                form.add_error('email',  'This email is already in use. Please choose a different email address.')
            else:
                try:
                    form.save()
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password1']
                    seeker = authenticate(request, email=email, password=password)
                    if seeker is not None and seeker.is_authenticated:
                        login(request, seeker)
                        messages.success(request, 'Registration Successfull! 🥳 🥂')
                        return redirect('seeker_csv_upload')
                    else:
                        messages.error(request, 'Authentication failed. 🚫')
                except IntegrityError:
                    form.add_error(None, 'Error occurred during registration.')
                
        context = {
            'registration_form': form,
            'messages': messages.get_messages(request)
        }
        
        return render(request, 'registration.html', context)


#TODO add a loding screen when seeker is logging in
class SeekerLoginView(View):
    def get(self, request):
        form = SeekerLoginForm()
        
        context = {
            'login_form': form
        }
        
        return render(request, 'login.html', context)
    
    def post(self, request):
        form = SeekerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            seeker = authenticate(request, email=email, password=password)
            if seeker is not None:
                login(request, seeker)
                messages.success(request, f'You are now logged in as {email} 👍')
                return redirect('seeker_dashboard')
            else:
                form.add_error(None, 'Email or Password is invalid please try again 🙅‍♂️')
            
        context = {
            'login_form': form
        }
        
        return render(request, 'login.html', context)


class SeekerLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logged Out! 🚪 👋')
        return render(request, 'logout.html')
    
    
#TODO add a loading screen when seeker is uploading a CSV
@method_decorator(login_required, name='dispatch') 
class SeekerCsvUploadView(View): 
    def get(self, request):
        form = SeekerCsvUploadForm()
        context = {
            'csv_form': form
        }
        return render(request, 'csv_upload.html', context)
    
    def post(self, request):
        form = SeekerCsvUploadForm(request.POST, request.FILES)
        
        # init created_csv_ids list if it doesn't exist in the session [bug fix 🦟]
        if 'created_csv_ids' not in request.session:
            request.session['created_csv_ids'] = []
            
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE! 🤦‍♂️ 😑')
                return redirect('seeker_csv_upload')
            
            #TODO add logic to skip empty rows
            try:
                decode_file = csv_file.read().decode('utf-8')
                csv_data = csv.reader(decode_file.splitlines(), delimiter=',')
                next(csv_data)
                next(csv_data)
                next(csv_data)
                next(csv_data)
                
                seeker = request.user
                # row_count = 0
                created_csv_ids = []
                
                for row in csv_data:
                    try:            
                        obj, created = Csv.objects.update_or_create(
                            first_name=row[0],
                            last_name=row[1],
                            company=row[4],
                            position=row[5],
                            seeker=seeker,
                        )
                        
                        if created:
                            created_csv_ids.append(obj.id)
                            
                        # row_count += 1
                        # if row_count >= 500:
                        #     break
                        
                    except IndexError:
                        messages.error(request, 'An error occurred: List index out of range, this is not a properly formated csv from LinkedIn. 🛑')
                        return redirect('seeker_csv_upload')
                    except StopIteration:
                        break
                
                request.session['created_csv_ids'].append(obj.id)
                messages.success(request, 'Upload Successful! 🥳')
                return render(request, 'upload_success.html')
            
            except UnicodeDecodeError:
                messages.error(request, 'THIS IS NOT A CSV FILE! 🤦‍♂️')
                return redirect('seeker_csv_upload')
        
        context = {
            'csv_form': form
        }
        
        return render(request, 'csv_upload.html', context)
    
    
@method_decorator(login_required, name='dispatch')
class SeekerTargetRolesTagsView(View):
    def get(self, request, search_query=None):
        form = SeekerTargetRolesTagsForm()
    
        context = {
            'roles_tags_form': form,
            'matched_tags': request.session.get('matched_tags', [])
        }
        
        return render(request, 'rolestags.html', context)
    
    def post(self, request):
        form = SeekerTargetRolesTagsForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            
            # Get all tags matching the search query from the user's CSV
            matching_tags = Csv.objects.filter(seeker=request.user, position__isnull=False, position__gt='', position__icontains=search_query).values_list('position', flat=True).distinct()
            
            # Retrieve the existing matched tags from the session
            matched_tags = set(request.session.get('matched_tags', []))
            
            # Append only the search term to the existing set
            for tag in matching_tags:
                if search_query.lower() in tag.lower():
                    matched_tags.add(search_query)
                    break
            
            # Convert the set back to a list
            matched_tags = list(matched_tags)[:5]
            
            # Update the matched tags in the session
            request.session['matched_tags'] = matched_tags 
            
            if len(matching_tags) > 0:
                messages.success(request, 'Tags matched successfully! 🥳')
            else:
                messages.warning(request, 'No matching tags found.  ❌ 😵')
                
            #TODO my issue is on line 222 I need to change the condition to check once we hit 5 added inputs to fire off this message warning and not matching_tags
            # print('matched_tags', matched_tags)
            # print('matching_tags', matching_tags)
            # if len(matching_tags) == 5:
            #     messages.warning(request, 'You have reached the tag limit')
            
            return redirect('seeker_roles_tags', search_query=search_query)


@login_required
def clear_tags(request):
    
    #TODO this is in relation to line 222
    # Logging before clearing the key value pair 
    # logging.info('Session before clearing matched_tags', request.session)
    # print('Session after clearing matched_tags', dict(request.session))
    
    if 'matched_tags' in request.session:
        del request.session['matched_tags']
    
    #TODO this is in relation to line 222
    # Logging after clearing the key value pair 
    # logging.info('Session after clearing matched_tags', request.session)
    # print('Session after clearing matched_tags', dict(request.session))
    
    return redirect('seeker_roles_tags')


class AddSeekerCSVContactInformationView(FormView):
    template_name = 'dashboard.html'
    
    def post(self, request, *args, **kwargs):
        form = AddSeekerCSVContactInformationForm(request.POST)
        
        if form.is_valid():
            cv_entry_id = kwargs.get('cv_entry_id')
            cv_entry = get_object_or_404(Csv, id=cv_entry_id)
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # Format and prepend '+' to the phone number
            phone_number = form.cleaned_data['phone_number']
            # formatted_phone_number = self.format_phone_number(phone_number)
            
            company= form.cleaned_data['company']
            position = form.cleaned_data['position']
            mini_bio = form.cleaned_data['mini_bio']
            notes = form.cleaned_data['notes']
    
            # Save the additional contact information to the CVEntry model instance
            cv_entry.first_name = first_name
            cv_entry.last_name = last_name
            cv_entry.email = email
            # cv_entry.phone_number = formatted_phone_number
            cv_entry.phone_number = phone_number
            cv_entry.company = company
            cv_entry.position = position
            cv_entry.mini_bio = mini_bio
            cv_entry.notes = notes
            cv_entry.save()
            
            # Redirect to a success page
            messages.success(request, 'Contact information added successfully ✅')
            return super().form_valid(form)
        else:
            print(form.errors)
            messages.error(request, f'Form is bad ❌ {form.errors}')
            return self.form_invalid(form)
            
    
    def get_success_url(self):
        # Add the URL to redirect to after successful form submission
        return reverse('seeker_dashboard')
