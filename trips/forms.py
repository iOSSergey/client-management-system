from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['client', 'start_date', 'end_date', 'destination', 'accommodation', 'price', 'notes']
