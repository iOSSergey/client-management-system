from django.shortcuts import render, get_object_or_404, redirect
from clients.models import Client
from django.urls import reverse
from .models import Trip
from .forms import TripForm

def trip_create(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.client = client
            trip.save()
            return redirect('client_detail', client_id=client.id)
    else:
        form = TripForm()
    return render(request, 'trips/trip_form.html', {'form': form, 'client': client})

def trip_update(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_list', client_id=trip.client.id)
    else:
        form = TripForm(instance=trip)
    return render(request, 'trips/trip_form.html', {'form': form})

def trip_list(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    trips = Trip.objects.filter(client=client)
    return render(request, 'trips/trip_list.html', {'trips': trips, 'client': client})


def trip_delete(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    trip.delete()
    return redirect(reverse('client_detail', args=[trip.client.id]))