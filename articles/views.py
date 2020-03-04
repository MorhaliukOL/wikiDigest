from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import CreateArticleForm
from .models import Article, Category

ARTICLES_PER_PAGE = 2


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
    category_obj = get_object_or_404(Category, name=category)

    # fix reverse ordering
    articles = Article.objects.filter(category=category_obj).order_by('-created')
    paginator = Paginator(articles, ARTICLES_PER_PAGE)
    page_number = request.GET.get('page')
    art_obj = paginator.get_page(page_number)
    context = {
        'art_obj': art_obj,
        'category': category
    }
    return render(request, 'articles/articles_list.html', context)


def article_details(request, title):
    article = get_object_or_404(Article, title=title)
    return render(request, 'articles/article_details.html', {'article': article})
