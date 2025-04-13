from django.db import models
from core.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('progress', 'In Progress'),
        ('done', 'Completed')
    ]
    
    order_id = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    department = models.ForeignKey('core.Department', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    due_time = models.DateTimeField()
    notes = models.TextField(blank=True)