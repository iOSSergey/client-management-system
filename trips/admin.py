from django.contrib import admin
from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ['client', 'start_date', 'end_date', 'destination', 'accommodation', 'price', 'notes']
    list_filter = ['client', 'start_date', 'end_date', 'destination']
    search_fields = ['destination', 'accommodation', 'notes']
    
admin.site.register(Trip, TripAdmin)
