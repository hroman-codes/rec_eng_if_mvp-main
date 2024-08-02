#TODO uncomment TEST once business logic grows from activity tracker  

# from django.test import TestCase
# from apps.seeker.models import ActivityTracker, Seeker
# from apps.seeker.tests.factories import SeekerFactory

# #TODO create a factory for Activity Tracker once business logic grows for this model
# class ActivityTrackerModelTest(TestCase):
#     def setUp(self):
#         self.seeker = SeekerFactory()
#         self.activity_tracker = ActivityTracker.objects.create(seeker=self.seeker)
    
#     def test_str_representation(self):
#         expected_str = f'ActivityTracker ID: {self.activity_tracker.id}'
#         self.assertEqual(str(self.activity_tracker), expected_str)
        