from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.seeker.tests.factories.seeker import SeekerFactory
        
class UserManagerModelTest(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user_manager = self.User.objects
        self.user = self.user_manager._create_user(email='heriberto@theseeker.ai', password='password')
        self.superuser = self.user_manager.create_superuser(email='heri@theseeker.ai', password='password')

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            self.user_manager._create_user(email='', password='password')

    def test_create_user(self):
        self.assertEqual(self.user.email, 'heriberto@theseeker.ai')
        self.assertTrue(self.user.check_password('password'))
        
    def test_create_user_with_email(self):
        # Use the same user_manager instance throughout the test case
        user = self.user_manager._create_user(email='test@example.com', password='password')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('password'))

    def test_create_superuser(self):
        self.assertTrue(self.superuser.is_superuser)
        self.assertTrue(self.superuser.is_staff)
        self.assertEqual(self.superuser.email, 'heri@theseeker.ai')
        self.assertTrue(self.superuser.check_password('password'))


class SeekerModelTest(TestCase):    
    def setUp(self):
        self.seeker = SeekerFactory()
        self.User = get_user_model()
        self.user_manager = self.User.objects
        
    def test_str_representation(self): 
        expected_str = str(self.seeker)
        self.assertEqual(str(self.seeker), expected_str)
        
    def test_default_referrer(self):
        self.assertFalse(self.seeker.referrer)
        
    def test_field_max_lengths(self):
        self.assertEqual(self.seeker._meta.get_field('first_name').max_length, 50)
        self.assertEqual(self.seeker._meta.get_field('last_name').max_length, 50)
        self.assertEqual(self.seeker._meta.get_field('phone_number').max_length, 20)
        self.assertEqual(self.seeker._meta.get_field('headline').max_length, 255)
        
    def test_upload_to_path(self):
        expected_path=self.seeker.resume.name
        self.assertEqual(self.seeker.resume.name, expected_path)
        
    def test_profile_photo_field_type(self):
        self.assertIsInstance(self.seeker.profile_photo, bytes)
        
    def test_valid_linkedin_urls(self):
        self.assertTrue(self.seeker.linkedin_url.startswith('https://'))
    
    def test_valid_calendly_urls(self):
        self.assertTrue(self.seeker.calendly_link.startswith('https://'))
        
        