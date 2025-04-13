from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'article_type', 'content', 'file']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }