from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .forms import CreateArticleForm
from .models import Article, Category


def create_article(request):
    if request.method == 'POST':
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
        else:
            messages.ERROR(request, 'Invalid data!!!')
    else:
        form = CreateArticleForm()
    return render(request, 'articles/create_article.html', {'form': form})


def show_articles_list(request, category):
    try:
        category_obj = Category.objects.get(name=category)
    except Category.DoesNotExist:
        raise Http404
    articles = Article.objects.filter(category=category_obj)
    context = {
        'articles': articles,
        'category': category
    }
    return render(request, 'articles/articles_list.html', context)


def article_details(request, title):
    try:
        print('the title:', title)
        article = Article.objects.get(title=title)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'articles/article_details.html', {'article': article})
