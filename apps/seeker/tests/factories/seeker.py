import os
import factory

from factory.django import DjangoModelFactory
from factory.faker import Faker as FakeFactory
from apps.seeker.models import Seeker

class SeekerFactory(DjangoModelFactory):
    class Meta:
        model = Seeker
    
    created_at = FakeFactory('date_time_this_decade')
    referrer = factory.Iterator([False])
    first_name = FakeFactory('first_name')
    last_name = FakeFactory('last_name')
    email = FakeFactory('email')
    password = FakeFactory('password')
    phone_number = FakeFactory('phone_number')
    headline = FakeFactory('job')
    summary = FakeFactory('text')
    profile_photo = FakeFactory('binary')
    linkedin_url = FakeFactory('url', schemes=['https'])
    calendly_link = FakeFactory('url', schemes=['https'])
 