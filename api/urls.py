# client_management_system/api/urls.py
from django.urls import path
from .views import ClientListView, TripListView, AllDataView, ManualView

urlpatterns = [
    path('v1/clients/', ClientListView.as_view(), name='client-list'),
    path('v1/trips/', TripListView.as_view(), name='trip-list'),
    path('v1/all_data/', AllDataView.as_view(), name='all-data'),
    path('manual/', ManualView.as_view(), name='api-manual'),  # Новый маршрут для manual
]
