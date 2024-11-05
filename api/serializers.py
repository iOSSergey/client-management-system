# Create serializers for the models Client and Trip
from rest_framework import serializers
from clients.models import Client
from trips.models import Trip


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
