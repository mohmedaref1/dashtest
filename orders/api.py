import random
from datetime import datetime, timedelta
from django.utils import timezone

class SallaAPI:
    def get_orders(self):
        # Simulate API response
        return [
            {
                'id': f"ORD-{random.randint(1000,9999)}",
                'customer_id': f"CUST-{random.randint(100,999)}",
                'department': random.choice(['Electronics', 'Fashion', 'Home']),
                'status': random.choice(['new', 'progress', 'completed']),
                'due_time': timezone.now() + timedelta(hours=random.randint(1, 72))
            } for _ in range(15)
        ]
    
    # Add other API methods with similar simulation