from django.test import TestCase
from django.urls import reverse

class CustomErrorViewTest(TestCase):     
    def test_custom_404_view(self):
        # Simulate a request to a non-existent URL
        response = self.client.get('/nonexistent-path/')

        # Assert that the response has a 404 status code
        self.assertEqual(response.status_code, 404)
        
    # def test_custom_500_view(self):
    #     # Simulate a request to the custom_500_view
    #     response = self.client.get(reverse('custom_500_view'))

    #     # Assert that the response has a 500 status code
    #     self.assertEqual(response.status_code, 500)