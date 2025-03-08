# forms.py
from django import forms
from .models import Services

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title', 'description', 'image', 'icon', 'is_active']
