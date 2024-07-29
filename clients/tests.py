from django.test import TestCase
from django.urls import reverse
from .models import Client

class ClientViewsTest(TestCase):
    def setUp(self):
        # Create test data
        Client.objects.create(first_name="John", last_name="Doe")
        Client.objects.create(first_name="Jane", last_name="Doe")
        # Add more clients for the test

    def test_latest_clients_view(self):
        response = self.client.get(reverse('latest_clients'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clients/latest_clients.html')
        self.assertTrue('clients' in response.context)
        # Check that no more than 5 clients are returned
        self.assertLessEqual(len(response.context['clients']), 5)
