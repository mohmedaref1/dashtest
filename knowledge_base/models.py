from django.db import models
from core.models import User

class Article(models.Model):
    ARTICLE_TYPES = [
        ('guide', 'Guide'),
        ('video', 'Video Tutorial'),
        ('policy', 'Policy')
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    article_type = models.CharField(max_length=20, choices=ARTICLE_TYPES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='knowledge/', blank=True)