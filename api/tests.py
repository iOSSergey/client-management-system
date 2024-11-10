from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from clients.models import Client
from trips.models import Trip

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client1 = Client.objects.create(first_name="John", last_name="Doe")
        self.trip1 = Trip.objects.create(destination="Paris", client=self.client1)

    def test_get_clients(self):
        response = self.client.get(reverse('client-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_trips(self):
        response = self.client.get(reverse('trip-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
