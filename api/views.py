from django.shortcuts import render

# Create api views here

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from clients.models import Client
from trips.models import Trip
from .serializers import ClientSerializer, TripSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class TripListView(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class AllDataView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        if 'clients' in request.query_params:
            clients = Client.objects.all()
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
        elif 'trips' in request.query_params:
            trips = Trip.objects.all()
            serializer = TripSerializer(trips, many=True)
            return Response(serializer.data)
        else:
            clients = Client.objects.all()
            trips = Trip.objects.all()
            client_serializer = ClientSerializer(clients, many=True)
            trip_serializer = TripSerializer(trips, many=True)
            return Response({
                'clients': client_serializer.data,
                'trips': trip_serializer.data
            })


class ManualView(APIView):
    def get(self, request):
        return render(request, 'api/manual.html')
