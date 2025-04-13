from django.urls import path
from . import views

app_name = 'knowledge'

urlpatterns = [
    path('', views.article_list, name='list'),  # This should exist
    path('new/', views.new_article, name='new_article'),
    path('search/', views.search_articles, name='search'),
    path('<int:article_id>/', views.view_article, name='view'),
]