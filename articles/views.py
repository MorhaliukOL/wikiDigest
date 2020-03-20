from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .forms import CreateArticleForm, CreateCategoryForm
from .models import Article, Category

ARTICLES_PER_PAGE = 4


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
    articles = Article.objects.filter(category=category_obj).order_by('-created')
    paginator = Paginator(articles, ARTICLES_PER_PAGE)
    page_number = request.GET.get('page')
    art_obj = paginator.get_page(page_number)
    subcategories = category_obj.get_children()

    if request.method == 'POST':
        new_category_ids = map(int, request.POST.getlist('category'))
        category_article = zip(new_category_ids, articles)
        # Find way to update categories in one DB request
        for category, article in category_article:
            article.category = Category.objects.get(id=category)
            article.save()

    context = {
        'art_obj': art_obj,
        'category': category_obj,
        'subcategories': subcategories,
    }
    return render(request, 'articles/articles_list.html', context)


def article_details(request, title):
    article = get_object_or_404(Article, title=title)
    return render(request, 'articles/article_details.html', {'article': article})


def create_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateCategoryForm()
    return render(request, 'articles/create_category.html', {'form': form})
