from django.contrib import admin
from .models import User, Department

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'department')
    
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)