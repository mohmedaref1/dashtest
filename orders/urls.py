from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_dashboard, name='list'),  # Changed name to 'list'
    path('refresh/', views.refresh_orders, name='refresh'),
    path('search/', views.search_orders, name='search'),
    path('<int:order_id>/', views.order_detail, name='detail'),
    path('notifications/', views.order_notifications, name='notifications'),
    path('filter/', views.filter_orders, name='filter'),
]