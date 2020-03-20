from django.urls import path
from .views import create_article, show_articles_list, article_details, create_category


urlpatterns = [
    path('create', create_article, name='create_article'),
    path('add', create_category, name='create_category'),
    path('<str:title>', article_details, name='article_details'),
    path('list/<str:category>', show_articles_list, name='articles_by_category'),
]
