#TODO uncomment model once business logic grows 
# from django.test import TestCase
# from apps.seeker.models import Seeker, TargetCompany
# from apps.seeker.tests.factories.target_company import TargetCompanyFactory
# from apps.seeker.tests.factories.seeker import SeekerFactory

# class TargetCompanyModelTest(TestCase):
#     def setUp(self):
#         self.seeker = SeekerFactory.create()
#         self.target_company = TargetCompanyFactory(seeker=self.seeker)
    
#     def test_str_representation(self):
#         expected_str=str(self.target_company)
#         self.assertEqual(str(self.target_company), expected_str)
        
#     def test_foreign_key_relationship(self):
#         self.assertIsInstance(self.target_company.seeker, Seeker)
        
#     def test_field_max_length(self):
#         max_length = self.target_company._meta.get_field('company_name').max_length
#         self.assertEqual(max_length, 255)
        