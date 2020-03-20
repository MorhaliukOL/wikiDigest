from datetime import date
from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateField(default=date.today)
    body = models.TextField()
    category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True)
    ratified = models.BooleanField(default=False)
    references = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'<{self.title}>'
