from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from .models import Client
from .forms import ClientForm
from datetime import datetime


def latest_clients(request):
    # Get the latest 5 clients ordered by ID
    clients = Client.objects.order_by('-id')[:5]
    return render(request, 'clients/latest_clients.html', {'clients': clients})


def top_clients(request):
    # Get the top 20 clients based on the number of trips
    clients = Client.objects.annotate(
        trip_count=Count('trips')).order_by('-trip_count')[:20]
    return render(request, 'clients/top_clients.html', {'clients': clients})


def client_detail(request, client_id):
    # Get the details of a specific client and their trips
    client = get_object_or_404(Client, id=client_id)
    trips = client.trips.all()  # Get all trips of the client
    return render(request, 'clients/client_detail.html', {'client': client, 'trips': trips})


def search_clients(request):
    # Get the filter type from the GET parameters, default to 'name' if not provided
    filter_by = request.GET.get('filter', 'name')
    # Get the search query from the GET parameters
    query = request.GET.get('q', '')
    # Get date range parameters from the GET request
    start_date_str = request.GET.get('start_date', '')
    end_date_str = request.GET.get('end_date', '')

    results = Client.objects.none()

    if filter_by == 'name' and query:
        results = Client.objects.filter(
            Q(last_name__icontains=query) |
            Q(first_name__icontains=query) |
            Q(middle_name__icontains=query)
        )
    elif filter_by == 'birthday' and start_date_str and end_date_str:
        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            results = Client.objects.filter(
                birth_date__range=(start_date, end_date))
        except ValueError:
            # Handle invalid date input
            results = Client.objects.none()
    elif filter_by == 'region' and query:
        results = Client.objects.filter(region__icontains=query)

    # Get unique regions for the dropdown list
    regions = Client.objects.values_list('region', flat=True).distinct().exclude(
        region__isnull=True).exclude(region='')

    # Render the template with the search results and filter type
    return render(request, 'clients/search_clients.html', {
        'query': query,
        'results': results,
        'filter_by': filter_by,
        'start_date': start_date_str,
        'end_date': end_date_str,
        'regions': regions,
    })


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            # Save the form data without committing to the database
            client = form.save(commit=False)

            # Get the client's IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                # If there are multiple IPs, take the first one
                client.ip_address = x_forwarded_for.split(',')[0].strip()
            else:
                # If the header is not present, use REMOTE_ADDR
                client.ip_address = request.META.get('REMOTE_ADDR')

            client.save()  # Save the client to the database
            # Redirect to the client list or another page
            return redirect('latest_clients')
    else:
        form = ClientForm()

    return render(request, 'clients/add_client.html', {'form': form})


def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', client_id=client.id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'clients/edit_client.html', {'form': form, 'client': client})
