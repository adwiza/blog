from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=50)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='when_published')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    when_published = models.DateField(default=timezone.now)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, related_name='posts', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
