from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'middle_name': forms.TextInput(attrs={'placeholder': 'Enter middle name'}),
            'mailing_name': forms.TextInput(attrs={'placeholder': 'Enter mailing name'}),
            'postal_code': forms.TextInput(attrs={'placeholder': 'Enter postal code'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter country'}),
            'region': forms.TextInput(attrs={'placeholder': 'Enter region'}),
            'city': forms.TextInput(attrs={'placeholder': 'Enter city'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter address'}),
            'work_phone': forms.TextInput(attrs={'placeholder': 'Enter work phone'}),
            'home_phone': forms.TextInput(attrs={'placeholder': 'Enter home phone'}),
            'mobile_phone': forms.TextInput(attrs={'placeholder': 'Enter mobile phone'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'Enter birth date', 'type': 'date'}),
            'passport_number': forms.TextInput(attrs={'placeholder': 'Enter passport number'}),
            'salutation': forms.TextInput(attrs={'placeholder': 'Enter salutation'}),
            'comments': forms.Textarea(attrs={'placeholder': 'Enter comments'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'send_email': forms.CheckboxInput(attrs={'placeholder': 'Send email'}),
            'is_active': forms.CheckboxInput(attrs={'placeholder': 'Is active'}),
        }
