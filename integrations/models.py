from django.db import models
from core.models import User

class APIIntegration(models.Model):
    AUTH_TYPES = [
        ('basic', 'Basic Auth'),
        ('oauth2', 'OAuth 2.0'),
        ('api_key', 'API Key'),
    ]
    
    name = models.CharField(max_length=100)
    base_url = models.URLField()
    auth_type = models.CharField(max_length=20, choices=AUTH_TYPES)
    api_key = models.CharField(max_length=255, blank=True)
    client_id = models.CharField(max_length=255, blank=True)
    client_secret = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name