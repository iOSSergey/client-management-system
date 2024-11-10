from django.test import TestCase
from django.urls import reverse
from .models import Trip
from clients.models import Client

class TripViewsTest(TestCase):
    def setUp(self):
        # Create test data
        self.client = Client.objects.create(first_name="John", last_name="Doe")
        Trip.objects.create(destination="Paris", client=self.client)

    def test_trip_list_view(self):
        response = self.client.get(reverse('trip_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips/trip_list.html')
        self.assertTrue('trips' in response.context)
