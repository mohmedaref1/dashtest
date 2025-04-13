from django.contrib.auth.models import AbstractUser
from django.db import models  # Add this line

class User(AbstractUser):
    ROLES = (
        ('admin', 'Administrator'),
        ('team', 'Team Member'),
        ('dev', 'Developer')
    )
    
    role = models.CharField(max_length=10, choices=ROLES, default='team')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    shift_start = models.TimeField(null=True)
    shift_end = models.TimeField(null=True)

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_team(self):
        return self.role == 'team'

    @property
    def is_dev(self):
        return self.role == 'dev'

class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name