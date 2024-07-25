from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email', 'is_active')
    search_fields = ('last_name', 'first_name', 'middle_name', 'email')
    list_filter = ('is_active', 'country')
