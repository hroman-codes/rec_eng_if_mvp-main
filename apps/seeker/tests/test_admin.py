from django.test import TestCase
from apps.seeker.models import Seeker, Csv
from django.test.client import RequestFactory
from django.contrib import admin 
from apps.seeker.admin import CsvAdmin, SeekerAdmin
from apps.seeker.tests.factories import CsvFactory, SeekerFactory

class AdminTest(TestCase):
    def setUp(self):
        self.user = Seeker.objects._create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.factory = RequestFactory()
        self.seeker = SeekerFactory()
        self.csv = CsvFactory(
            first_name=self.seeker.first_name,
            last_name=self.seeker.last_name,
            email=self.seeker.email,
            company='the seeker',
            position='software engineer',
            mini_bio='sample bio',
            notes='sample notes',
            seeker_id=self.seeker.id
        )
    
    def test_has_delete_permission_false(self):
        # Create a request
        request = self.factory.get('/admin/csv/')
        request.user = self.user

        # Initialize the CsvAdmin with the Csv model and admin site
        admin_instance = CsvAdmin(Csv, admin.site)
        has_permission = admin_instance.has_delete_permission(request, self.csv)

        # Assert that has_delete_permission returns True for the user
        self.assertFalse(has_permission)
        
    def test_get_displayed_password(self):
        # Initialize the SeekerAdmin class
        admin_instance = SeekerAdmin(Seeker, admin.site)

        # Call the get_displayed_password method
        displayed_password = admin_instance.get_displayed_password(self.seeker)

        # Define the expected displayed password (masked)
        expected_displayed_password = '********'

        # Assert that the displayed password matches the expected value
        self.assertEqual(displayed_password, expected_displayed_password)
        