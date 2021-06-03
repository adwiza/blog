from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post


class PostsListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    template = 'posts/list.html'
