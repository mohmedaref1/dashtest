from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('manage/', views.team_management, name='manage'),
    path('shift/start/', views.shift_start, name='shift_start'),
    path('shift/end/', views.shift_end, name='shift_end'),
    path('add/', views.add_member, name='add_member'),
    path('edit/<int:member_id>/', views.edit_member, name='edit_member'),
    path('delete/<int:member_id>/', views.delete_member, name='delete_member'),
    path('popup/close/', views.close_popup, name='close_popup'),
]