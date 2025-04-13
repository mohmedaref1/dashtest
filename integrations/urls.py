from django.urls import path
from . import views

app_name = 'integrations'

urlpatterns = [
    path('', views.integrations_dashboard, name='dashboard'),
    path('new/', views.create_integration, name='create'),
    path('test/<int:integration_id>/', views.test_integration, name='test'),
]