import re
from django.test import TestCase
from apps.seeker.forms import SeekerRegistrationForm, AddSeekerCSVContactInformationForm

class SeekerRegistrationFormTest(TestCase):
    def test_valid_form(self):
        # Create a valid form data dictionary
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

        # Initialize the form with the valid data
        form = SeekerRegistrationForm(data=form_data)

        # Check that the form is valid
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        # Create an invalid form data dictionary with missing required fields
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',  
            'email': 'invalid-email',  
            'password1': 'secure_password123',  
            'password2': 'password123',
        }

        # Initialize the form with the invalid data
        form = SeekerRegistrationForm(data=form_data)

        # Check that the form is not valid
        self.assertFalse(form.is_valid())

        # Use a regular expression to check for the error message
        expected_error_message = r"The two password fields .* match\." 
        self.assertRegex(form.errors.get('password2')[0], expected_error_message)

        
    def test_field_attributes(self):
        form = SeekerRegistrationForm()

        # Check that the field widgets have the expected attributes
        self.assertEqual(form.fields['first_name'].widget.attrs, {'maxlength': '50', 'class': 'form-control'})
        self.assertEqual(form.fields['last_name'].widget.attrs, {'maxlength': '50', 'class': 'form-control'})
        self.assertEqual(form.fields['email'].widget.attrs, {'maxlength': '254', 'class': 'form-control', 'autofocus': True})
        self.assertEqual(form.fields['password1'].widget.attrs, {'autocomplete': 'new-password', 'class': 'form-control'})
        self.assertEqual(form.fields['password2'].widget.attrs, {'autocomplete': 'new-password', 'class': 'form-control'})
        

    def test_password_length_validation(self):
        # Test password length less than 8 characters
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'short',  # Password is too short
            'password2': 'short',  # Passwords don't match but that's not the focus here
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password1', form.errors)  # Check if 'password1' field has an error

        # Test password length equal to 8 characters
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': '8charspwd',  # Valid password length
            'password2': '8charspwd',  # Passwords match
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_first_name_validation(self):
        # Test first name length less than 3 characters
        form_data = {
            'first_name': 'Jo',  # First name is too short
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'secure_password123',
            'password2': 'secure_password123',
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

        # Test first name length greater than 50 characters
        form_data = {
            'first_name': 'JohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohn',  # First name is too long
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'secure_password123',
            'password2': 'secure_password123',
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

        # Test first name containing non-alphabetic characters
        form_data = {
            'first_name': 'John123',  # First name contains non-alphabetic characters
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'secure_password123',
            'password2': 'secure_password123',
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_last_name_validation(self):
        # Test last name length less than 3 characters
        form_data = {
            'first_name': 'John',
            'last_name': 'Do',  # Last name is too short
            'email': 'johndoe@example.com',
            'password1': 'secure_password123',
            'password2': 'secure_password123',
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)

        # Test last name length greater than 50 characters
        form_data = {
            'first_name': 'John',
            'last_name': 'DoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoeDoe',  # Last name is too long
            'email': 'johndoe@example.com',
            'password1': 'secure_password123',
            'password2': 'secure_password123',
        }
        form = SeekerRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)
