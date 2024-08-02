from django.db import models
from apps.seeker.models.seeker import Seeker
from phonenumber_field.modelfields import PhoneNumberField

#TODO When I deleted all the csvs from the admin for a specific user it also deleted the seeker account with it
#TODO need to figure out how can I delete all CSVs in the admin without it deleting a seeker account as well
#TODO In the admin file i added this function for now to prevent deletion def has_delete_permission
#TODO ass a custom phone number validator PhoneNumberField is giving me trouble with the +{phonenumber}
class Csv(models.Model): 
    first_name = models.CharField(max_length=255, default='', blank=True)
    last_name = models.CharField(max_length=255, default='', blank=True)
    email = models.CharField(max_length=255, default='', blank=True)
    phone_number = PhoneNumberField(default='', blank=True)
    company = models.CharField(max_length=255, default='', blank=True)
    position = models.CharField(max_length=255, default='', blank=True)
    mini_bio = models.CharField(max_length=255, default='', blank=True)
    notes = models.TextField(default='', blank=True, verbose_name='Notes')
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()
        self.email = self.email.lower()
        self.company = self.company.lower()
        self.position = self.position.lower()
        self.mini_bio = self.mini_bio.lower()
        self.notes = self.notes.lower()
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
