from django.urls import path
from . import views

urlpatterns = [
    # The `trip_list` view is deprecated. Redirects to the client's detail page.
    # path('list/<int:client_id>/', views.trip_list, name='trip_list'),  
    path('create/<int:client_id>/', views.trip_create, name='trip_create'),
    path('update/<int:pk>/', views.trip_update, name='trip_update'),
    path('delete/<int:pk>/', views.trip_delete, name='trip_delete'),
]
