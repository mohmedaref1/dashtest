from django.contrib import admin
from .models import APIIntegration

@admin.register(APIIntegration)
class APIIntegrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'auth_type', 'created_by', 'is_active')
    list_filter = ('auth_type', 'is_active')