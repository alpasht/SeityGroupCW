from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'department', 'manager', 'manager_email', 'members_count', 'skills', 'upstream_count', 'downstream_count']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Platform Core'}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Engineering'}),
            'manager': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'manager_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'manager@sky.uk'}),
            'members_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python, Django, React...'}),
            'upstream_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'downstream_count': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
