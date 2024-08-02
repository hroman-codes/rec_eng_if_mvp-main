import factory

from apps.seeker.models import Csv
from factory.django import DjangoModelFactory
from apps.seeker.tests.factories import SeekerFactory

class CsvFactory(DjangoModelFactory):
    class Meta:
        model = Csv
    
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    company = factory.Faker('company')
    position = factory.Faker('job')
    seeker_id = factory.SubFactory(SeekerFactory)
