from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest_clients, name='latest_clients'),
    path('top-clients/', views.top_clients, name='top_clients'), 
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('search/', views.search_clients, name='search_clients'),
    path('add-client/', views.add_client, name='add_client'),
]

