# trips/forms.py
from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['start_date', 'end_date', 'destination', 'accommodation', 'price', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'destination': forms.TextInput(attrs={'placeholder': 'Enter destination'}),
            'accommodation': forms.TextInput(attrs={'placeholder': 'Enter accommodation'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Additional notes'}),
        }

    def __init__(self, *args, **kwargs):
        super(TripForm, self).__init__(*args, **kwargs)
        if not self.instance.pk:  # if the form is being used to create a new instance
            self.fields['price'].initial = 10000