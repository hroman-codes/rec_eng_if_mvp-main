#TODO uncomment model once business logic grows
# from django.test import TestCase
# from apps.seeker.models import TargetRole, Seeker
# from apps.seeker.tests.factories import TargetRoleFactory, SeekerFactory

# class TargetRoleTest(TestCase):
#     def setUp(self):
#         self.seeker = SeekerFactory(first_name='Heriberto')
#         self.target_role = TargetRoleFactory(seeker=self.seeker, role='SWE')
        
#     def test_role_label(self):
#         target_role = TargetRole.objects.get(id=1)
#         field_label = target_role._meta.get_field('role').verbose_name
#         self.assertEqual(field_label, 'role')
        
#     def test_role_max_length(self):
#         target_role = TargetRole.objects.get(id=1)
#         max_length = target_role._meta.get_field('role').max_length
#         self.assertEqual(max_length, 255)
    
#     def test_string_representation(self):
#         target_role = TargetRole.objects.get(id=1)
#         self.assertEqual(str(target_role), 'TargetRole ID: 1')
        
#     def test_seekers_relationship(self):
#         target_role = TargetRole.objects.get(id=1)
#         related_seeker = target_role.seeker
#         self.assertIsInstance(related_seeker, Seeker)
#         self.assertEqual(related_seeker.first_name, 'Heriberto')
        