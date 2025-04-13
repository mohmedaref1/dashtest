from django.shortcuts import render, get_object_or_404
from django_htmx.http import trigger_client_event
from .models import Order
from .api import SallaAPI
from django.contrib.auth.decorators import login_required

@login_required
def order_dashboard(request):
    api = SallaAPI()
    orders = api.get_orders()  # Will use mock data until API ready
    return render(request, 'orders/dashboard.html', {'orders': orders})

@login_required
def refresh_orders(request):
    api = SallaAPI()
    orders = api.get_orders()
    response = render(request, 'orders/partials/orders_grid.html', {'orders': orders})
    trigger_client_event(response, 'orders-updated')
    return response

@login_required
def search_orders(request):
    query = request.GET.get('q', '')
    api = SallaAPI()
    orders = api.search_orders(query)
    return render(request, 'orders/partials/orders_grid.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    api = SallaAPI()
    order = api.get_order(order_id)
    return render(request, 'orders/detail.html', {'order': order})

@login_required
def order_notifications(request):
    api = SallaAPI()
    new_orders = api.get_new_orders()
    return render(request, 'orders/partials/notifications.html', {'orders': new_orders})

@login_required
def filter_orders(request):
    status = request.GET.get('status', 'all')
    api = SallaAPI()
    orders = api.get_orders_by_status(status)
    return render(request, 'orders/partials/orders_grid.html', {'orders': orders})