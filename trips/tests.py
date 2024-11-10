from django.test import TestCase
from django.urls import reverse
from .models import Trip
from clients.models import Client

class TripViewsTest(TestCase):
    def setUp(self):
        # Create test data
        self.client_instance = Client.objects.create(first_name="John", last_name="Doe")
        Trip.objects.create(destination="Paris", client=self.client_instance)


