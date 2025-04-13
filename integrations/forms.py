from django import forms
from .models import APIIntegration

class APIIntegrationForm(forms.ModelForm):
    class Meta:
        model = APIIntegration
        fields = ['name', 'base_url', 'auth_type', 'api_key', 'client_id', 'client_secret']
        widgets = {
            'client_secret': forms.PasswordInput(render_value=True),
            'api_key': forms.PasswordInput(render_value=True),
        }