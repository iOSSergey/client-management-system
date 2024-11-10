from django.db import models
from django.utils import timezone
# Assuming the Client model is in the clients app
from clients.models import Client
from datetime import date


class Trip(models.Model):
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='trips')
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    destination = models.CharField(max_length=255)
    accommodation = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    notes = models.TextField(null=True, blank=True)

    # class Meta:
    #     db_table = 'ClientTrips'
