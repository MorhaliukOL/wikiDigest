from django import forms
from .models import Article, Category


class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'body', 'category', 'references']


class CreateCategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'parent']
