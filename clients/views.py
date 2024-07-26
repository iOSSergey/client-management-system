# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import Client
from django.db.models import Q
from .forms import ClientForm


def latest_clients(request):
    # Получаем последних 5 клиентов по дате создания
    clients = Client.objects.order_by('-id')[:5]
    return render(request, 'clients/latest_clients.html', {'clients': clients})


def top_clients(request):
    clients = Client.objects.annotate(trip_count=Count('trips')).order_by('-trip_count')[:20]
    return render(request, 'clients/top_clients.html', {'clients': clients})


def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    trips = client.trips.all()  # Получаем все поездки клиента
    return render(request, 'clients/client_detail.html', {'client': client, 'trips': trips})


def search_clients(request):
    query = request.GET.get('q', '')
    if query:
        results = Client.objects.filter(
            last_name__icontains=query
        ) | Client.objects.filter(
            first_name__icontains=query
        ) | Client.objects.filter(
            middle_name__icontains=query
        )
    else:
        results = []
    
    return render(request, 'clients/search_clients.html', {
        'query': query,
        'results': results,
    })


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Переадресация на список клиентов (или другую нужную вам страницу)
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form': form})
