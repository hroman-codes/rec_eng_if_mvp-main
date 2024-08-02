from factory.django import DjangoModelFactory
from factory.faker import Faker as FakeFactory
from apps.seeker.models import Csv

class CompanyFactory(DjangoModelFactory):
    class Meta:
        model = Csv
    
    company = FakeFactory('company')
    mini_bio = FakeFactory('text')
    notes = FakeFactory('text')
 