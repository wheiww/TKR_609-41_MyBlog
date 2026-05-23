from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from articles.models import Article
from articles import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, template_name='articles/article_list.html', context={'articles': articles})


def article_item(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, template_name='articles/article_item.html', context={'article': article})


@login_required(login_url='accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = forms.CreateArticle()
    return render(request, template_name='articles/article_create.html', context={'form': form})