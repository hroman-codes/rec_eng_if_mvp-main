from django.contrib.auth import SESSION_KEY
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from apps.seeker.models import Csv, Seeker


class WorkspaceViewTests(TestCase):
    def setUp(self):
        self.user = Seeker.objects._create_user(email='owner@example.com', password='test-password-123', first_name='Jordan')
        self.other = Seeker.objects._create_user(email='other@example.com', password='other-password-123')
        self.contact = Csv.objects.create(seeker=self.user, first_name='Alex', last_name='Morgan', company='Acme', position='Software Engineer', notes='Original notes')
        self.private = Csv.objects.create(seeker=self.other, first_name='Private', last_name='Contact', position='Software Engineer')
        self.client.force_login(self.user)
        self.set_tags(['Engineer'])

    def set_tags(self, tags):
        session = self.client.session
        session['matched_tags'] = tags
        session.save()

    def upload(self, content, name='connections.csv'):
        return self.client.post(reverse('seeker_csv_upload'), {'csv_file': SimpleUploadedFile(name, content)}, follow=True)

    def test_dashboard_only_shows_current_users_connections(self):
        response = self.client.get(reverse('seeker_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual([c.pk for c in response.context['cv_entries']], [self.contact.pk])
        self.assertNotContains(response, 'Private Contact')
        self.assertEqual(list(response.context['messages']), [])

    def test_no_tags_has_clear_empty_state(self):
        self.set_tags([])
        response = self.client.get(reverse('seeker_dashboard'))
        self.assertContains(response, 'Start with a role tag')
        self.assertEqual(len(response.context['cv_entries']), 0)

    def test_no_connections_has_import_action(self):
        self.contact.delete()
        response = self.client.get(reverse('seeker_dashboard'))
        self.assertContains(response, 'Bring your network into focus')
        self.assertContains(response, 'Upload your CSV')

    def test_unmatched_tags_has_clear_empty_state(self):
        self.set_tags(['Astronaut'])
        self.assertContains(self.client.get(reverse('seeker_dashboard')), 'No connections match yet')

    def test_tags_match_any_role(self):
        second = Csv.objects.create(seeker=self.user, first_name='Riley', position='Founder')
        self.set_tags(['Engineer', 'Founder'])
        response = self.client.get(reverse('seeker_dashboard'))
        self.assertEqual({c.pk for c in response.context['cv_entries']}, {self.contact.pk, second.pk})

    def test_contact_selection_and_edit_initial_values(self):
        response = self.client.get(reverse('seeker_dashboard'), {'edit': self.contact.pk})
        self.assertEqual(response.context['selected_contact'], self.contact)
        self.assertEqual(response.context['contact_form'].initial['first_name'], 'alex')
        self.assertContains(response, 'Save changes')

    def test_other_users_contact_cannot_be_selected_or_edited(self):
        for parameter in ('edit', 'contact'):
            with self.subTest(parameter=parameter):
                self.assertEqual(self.client.get(reverse('seeker_dashboard'), {parameter: self.private.pk}).status_code, 404)
        response = self.client.post(reverse('add_contact_info', args=[self.private.pk]), {'notes': 'Changed'})
        self.assertEqual(response.status_code, 404)
        self.private.refresh_from_db()
        self.assertEqual(self.private.notes, '')

    def test_invalid_contact_id_returns_404(self):
        self.assertEqual(self.client.get(reverse('seeker_dashboard'), {'contact': 'not-an-id'}).status_code, 404)

    def test_editor_saves_database_backed_contact(self):
        response = self.client.post(reverse('add_contact_info', args=[self.contact.pk]), {
            'first_name': 'Alex', 'last_name': 'Morgan', 'company': 'Acme',
            'position': 'Software Engineer', 'email': 'alex@example.com',
            'phone_number': '+12125552368', 'mini_bio': 'Builds useful tools.',
            'notes': 'Follow up next Tuesday.',
        }, follow=True)
        self.assertContains(response, 'Contact details saved.')
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.notes, 'Follow up next Tuesday.')
        self.assertEqual(self.contact.email, 'alex@example.com')
        self.assertEqual(response.context['selected_contact'], self.contact)

    def test_invalid_contact_form_preserves_values_and_context(self):
        response = self.client.post(reverse('add_contact_info', args=[self.contact.pk]), {'email': 'invalid', 'notes': 'Unsaved draft'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Unsaved draft')
        self.assertTrue(response.context['editing'])
        self.assertIn('email', response.context['contact_form'].errors)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.notes, 'Original notes')

    def test_long_contact_field_rejected(self):
        response = self.client.post(reverse('add_contact_info', args=[self.contact.pk]), {'mini_bio': 'a' * 256})
        self.assertIn('mini_bio', response.context['contact_form'].errors)

    def test_anonymous_workspace_routes_require_login(self):
        self.client.logout()
        for route in ('seeker_dashboard', 'seeker_csv_upload', 'seeker_roles_tags'):
            with self.subTest(route=route):
                response = self.client.get(reverse(route))
                self.assertEqual(response.status_code, 302)
                self.assertTrue(response.url.startswith(reverse('seeker_login')))
        self.assertEqual(self.client.post(reverse('add_contact_info', args=[self.contact.pk]), {'notes': 'Changed'}).status_code, 302)

    def test_csv_import_reads_all_rows_and_email(self):
        response = self.upload(b'First Name,Last Name,Company,Position,Email Address\nSam,Chen,Forma,Designer,sam@example.com\nRiley,Patel,Orbit,Founder,\n')
        self.assertRedirects(response, reverse('seeker_roles_tags'))
        self.assertEqual(Csv.objects.filter(seeker=self.user).count(), 3)
        self.assertEqual(Csv.objects.get(first_name='sam').email, 'sam@example.com')
        self.assertContains(response, 'Imported 2 connections')

    def test_linkedin_preamble_bom_blank_lines_and_quoted_company(self):
        content = '\ufeffNotes:\nExported connections\n\nFirst Name,Last Name,URL,Email Address,Company,Position,Connected On\nSam,Chen,https://example.com,sam@example.com,"Company, Inc",Designer,01 Jan 2026\n'
        self.upload(content.encode('utf-8'))
        self.assertEqual(Csv.objects.get(first_name='sam').company, 'company, inc')

    def test_reimport_does_not_duplicate_or_erase_notes_and_email(self):
        self.contact.email = 'alex@example.com'
        self.contact.save()
        content = b'first_name,last_name,company,position\nAlex,Morgan,Acme,Software Engineer\n'
        self.upload(content)
        self.upload(content)
        self.assertEqual(Csv.objects.filter(seeker=self.user).count(), 1)
        self.contact.refresh_from_db()
        self.assertEqual(self.contact.notes, 'Original notes')
        self.assertEqual(self.contact.email, 'alex@example.com')

    def test_malformed_csv_does_not_partially_import(self):
        response = self.upload(b'First Name,Last Name,Company,Position\nSam,Chen,Forma,Designer\nBroken,Row\n')
        self.assertContains(response, 'missing or extra columns')
        self.assertEqual(Csv.objects.filter(seeker=self.user).count(), 1)

    def test_invalid_csv_variants(self):
        cases = [
            ('wrong.txt', b'text'),
            ('invalid.csv', b'\xff\xfe'),
            ('noheaders.csv', b'First,Last\nSam,Chen'),
            ('empty.csv', b'First Name,Last Name,Company,Position\n'),
            ('too-big.csv', b'a' * (5 * 1024 * 1024 + 1)),
            ('long.csv', ('First Name,Last Name,Company,Position\nSam,Chen,Forma,' + 'a' * 256).encode()),
        ]
        for name, content in cases:
            with self.subTest(name=name):
                response = self.upload(content, name)
                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.context['csv_form'].errors)
                self.assertEqual(Csv.objects.filter(seeker=self.user).count(), 1)

    def test_add_tag_preserves_order_and_allows_unmatched_roles(self):
        self.client.post(reverse('seeker_roles_tags'), {'search_query': 'Founder'})
        self.assertEqual(self.client.session['matched_tags'], ['Engineer', 'Founder'])

    def test_tag_limit_duplicate_and_blank_validation(self):
        response = self.client.post(reverse('seeker_roles_tags'), {'search_query': 'engineer'})
        self.assertContains(response, 'already selected')
        response = self.client.post(reverse('seeker_roles_tags'), {'search_query': ' '})
        self.assertTrue(response.context['roles_tags_form'].errors)
        self.set_tags(['One', 'Two', 'Three', 'Four', 'Five'])
        response = self.client.post(reverse('seeker_roles_tags'), {'search_query': 'Six'})
        self.assertContains(response, 'up to five tags')
        self.assertEqual(len(self.client.session['matched_tags']), 5)

    def test_remove_and_clear_tags(self):
        self.set_tags(['Engineer', 'Founder'])
        self.client.post(reverse('seeker_roles_tags'), {'remove': 'Engineer'})
        self.assertEqual(self.client.session['matched_tags'], ['Founder'])
        self.assertEqual(self.client.get(reverse('clear_tags')).status_code, 405)
        self.client.post(reverse('clear_tags'))
        self.assertNotIn('matched_tags', self.client.session)

    def test_logout_requires_post(self):
        self.assertEqual(self.client.get(reverse('seeker_logout')).status_code, 405)
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertRedirects(self.client.post(reverse('seeker_logout')), reverse('seeker_login'))
        self.assertNotIn(SESSION_KEY, self.client.session)

    def test_mutations_require_csrf(self):
        strict = Client(enforce_csrf_checks=True)
        strict.force_login(self.user)
        for url in [reverse('seeker_logout'), reverse('clear_tags'), reverse('seeker_roles_tags'), reverse('seeker_csv_upload'), reverse('add_contact_info', args=[self.contact.pk])]:
            with self.subTest(url=url):
                self.assertEqual(strict.post(url, {'notes': 'unsafe'}).status_code, 403)


class AuthenticationViewTests(TestCase):
    def test_public_forms_render(self):
        for route in ('seeker_login', 'seeker_registration'):
            response = self.client.get(reverse(route))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'csrfmiddlewaretoken')

    def test_registration_creates_real_account_and_starts_import(self):
        response = self.client.post(reverse('seeker_registration'), {
            'first_name': 'Jordan', 'last_name': 'Rivera', 'email': 'jordan@example.com',
            'password1': 'Strong-test-pass-732', 'password2': 'Strong-test-pass-732',
        })
        self.assertRedirects(response, reverse('seeker_csv_upload'))
        user = Seeker.objects.get(email='jordan@example.com')
        self.assertTrue(user.check_password('Strong-test-pass-732'))
        self.assertEqual(int(self.client.session[SESSION_KEY]), user.pk)

    def test_duplicate_registration_and_password_mismatch(self):
        Seeker.objects._create_user(email='jordan@example.com', password='existing')
        response = self.client.post(reverse('seeker_registration'), {
            'first_name': 'Jordan', 'last_name': 'Rivera', 'email': 'jordan@example.com',
            'password1': 'Strong-test-pass-732', 'password2': 'different',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['registration_form'].errors)
        self.assertEqual(Seeker.objects.count(), 1)
        self.assertNotIn(SESSION_KEY, self.client.session)

    def test_valid_login_and_invalid_login(self):
        Seeker.objects._create_user(email='jordan@example.com', password='Strong-test-pass-732')
        response = self.client.post(reverse('seeker_login'), {'email': 'jordan@example.com', 'password': 'wrong'})
        self.assertContains(response, 'Email or password is incorrect')
        self.assertNotIn(SESSION_KEY, self.client.session)
        response = self.client.post(reverse('seeker_login'), {'email': 'jordan@example.com', 'password': 'Strong-test-pass-732'})
        self.assertRedirects(response, reverse('seeker_dashboard'))
        self.assertIn(SESSION_KEY, self.client.session)

    def test_authentication_forms_require_csrf(self):
        strict = Client(enforce_csrf_checks=True)
        for route in ('seeker_login', 'seeker_registration'):
            self.assertEqual(strict.post(reverse(route), {}).status_code, 403)

    def test_health_endpoint(self):
        response = self.client.get(reverse('health'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'ok'})
