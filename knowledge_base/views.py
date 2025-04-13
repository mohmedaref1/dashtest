from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

@login_required
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'knowledge/list.html', {'articles': articles})

@login_required
def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('knowledge:view', article.id)
    else:
        form = ArticleForm()
    return render(request, 'knowledge/form.html', {'form': form})

@login_required
def search_articles(request):
    query = request.GET.get('q', '')
    articles = Article.objects.filter(title__icontains=query)
    return render(request, 'knowledge/partials/results.html', {'articles': articles})

@login_required
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'knowledge/detail.html', {'article': article})