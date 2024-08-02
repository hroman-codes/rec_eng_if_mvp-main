import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from apps.seeker.models import Seeker, Csv
from phonenumber_field.formfields import PhoneNumberField
from django.utils.safestring import mark_safe


class SeekerRegistrationForm(UserCreationForm):
    # Add custom widget attribute customizations for each field 
    #TODO This was created in order to pass testcase need to clean this up line 12-29
    #DELETE THIS IF THE REGISTRATION FORM BREAKS
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'maxlength': '50'
            }),
        )
    first_name.label = mark_safe('<i class="bi bi-person-circle"></i> First Name')
    
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '50'}),
    )
    
    last_name.label = mark_safe('<i class="bi bi-person-circle"></i> Last Name')
    
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'maxlength': '254', 'autofocus': True}),
    )
    
    email.label = mark_safe('<i class="bi bi-envelope"></i> Email')
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
    )
    
    password1.label = mark_safe('<i class="bi bi-file-lock2"></i> Create Password')
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
    )
    
    password2.label = mark_safe('<i class="bi bi-file-lock-fill"></i> Confirm Password')
    
    class Meta(UserCreationForm.Meta):
        model = Seeker
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
     
    # if registration breaks delete this method   
    def clean_password1(self):
        # Get the 'password1' field value
        password1 = self.cleaned_data.get('password1')

        # Check if the password meets the minimum length requirement (e.g., 8 characters)
        if len(password1) < 8:
            raise forms.ValidationError('Password should be at least 8 characters long.')

        return password1
        
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # VALIDATION 
        if first_name and (len(first_name) < 3 or len(first_name) > 50):
            self.add_error('first_name', 'First name is too short or too long.')
        elif first_name and not re.match(r'^[A-Za-z]+$', first_name):
            self.add_error('first_name', 'First name should only contain alphabetic characters.')
        
        if last_name and (len(last_name) < 3 or len(last_name) > 50):
            self.add_error('last_name', 'Last name is too short or too long.')
        elif last_name and not re.match(r'^[A-Za-z]+$', last_name):
            self.add_error('last_name', 'Last name should only contain alphabetic characters.')
        
        if not email:
            self.add_error('email', 'Email field is required.')
       
        if password and len(password) < 8:
            self.add_error('password', 'Password should be at least 8 characters long.')

        return cleaned_data


class SeekerLoginForm(forms.Form):
    # email = forms.EmailField(label='Email')
    
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'maxlength': '254', 
            'autofocus': True
            }),
        )
    email.label = mark_safe('<i class="bi bi-envelope"></i> Email')
    
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
            })
        )
    password.label = mark_safe('<i class="bi bi-file-lock2"></i> Password')
    

        
class SeekerCsvUploadForm(forms.Form):
    csv_file = forms.FileField(label='Upload CSV')
    

class SeekerTargetRolesTagsForm(forms.Form):
    search_query = forms.CharField(
        label='Search', 
        max_length='50',
        widget=forms.TextInput(attrs={'placeholder': 'Enter tag', 'class':"form-control"}),
    )


class AddSeekerCSVContactInformationForm(forms.Form):
    first_name = forms.CharField(label='First Name', required=False)
    last_name = forms.CharField(label='Last Name', required=False)
    email = forms.EmailField(label='Email', required=False)
    phone_number = PhoneNumberField(label='Phone Number', required=False)
    company = forms.CharField(label='Company', required=False)
    position = forms.CharField(label='Position', required=False)
    mini_bio =  forms.CharField(label='Mini Bio', required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False, label='Notes')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a valid phone number (e.g. +12125552368)'})
        self.fields['company'].widget.attrs.update({'class': 'form-control'})
        self.fields['position'].widget.attrs.update({'class': 'form-control'})
        self.fields['mini_bio'].widget.attrs.update({'class': 'form-control'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control'})
        