from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = forms.ArticleForm()
    return render(request, template_name='articles/article_form.html', context={'form': form})


@login_required(login_url='accounts:login')
def article_update(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user.id == article.author.id:
        if request.method == 'POST':
            form = forms.ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect(to='articles:article_detail', slug=article.slug)
        else:
            form = forms.ArticleForm(instance=article)
        return render(request, template_name='articles/article_form.html', context={'form': form})
    return HttpResponse(content='401 Unauthorized', status=401)


@login_required(login_url='accounts:login')
def article_delete(request, slug):
    article = Article.objects.get(slug=slug)
    if request.user.id == article.author.id:
        if request.method == 'POST':
            article.delete()
            return redirect('homepage')
        return render(request, template_name='articles/article_confirm_delete.html', context={'article': article})
    return HttpResponse(content='401 Unauthorized', status=401)