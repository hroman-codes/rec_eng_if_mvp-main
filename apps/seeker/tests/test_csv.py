from django.test import TestCase
from apps.seeker.models import Csv
from apps.seeker.tests.factories import CsvFactory, SeekerFactory

#TODO create a Factory for companies and inject into code
#TODO create a factory for positions and inject into code base
class CsvModelTest(TestCase):
    def setUp(self):
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
    
    def test_csv_creation(self):
        self.assertEqual(self.csv.first_name, self.seeker.first_name.lower())
        self.assertEqual(self.csv.last_name, self.seeker.last_name.lower())
        self.assertEqual(self.csv.email, self.seeker.email)
        self.assertTrue(self.csv.company)
        self.assertTrue(self.csv.position)
        self.assertEqual(self.csv.seeker_id, self.seeker.id)
        
    def test_save_method_lowercase_fields(self):
        self.csv.save()
        saved_csv = Csv.objects.get(pk=self.csv.pk)
        
        self.assertEqual(saved_csv.first_name, self.seeker.first_name.lower())
        self.assertEqual(saved_csv.last_name, self.seeker.last_name.lower())
        self.assertEqual(saved_csv.email, self.seeker.email)
        self.assertEqual(saved_csv.company, 'the seeker')
        self.assertEqual(saved_csv.position, 'software engineer')
        self.assertEqual(saved_csv.mini_bio, 'sample bio')
        self.assertEqual(saved_csv.notes, 'sample notes')
        
    def test_str_representation(self):
        self.assertEqual(str(self.csv), f"{self.seeker.first_name.lower()} {self.seeker.last_name.lower()}" )
        