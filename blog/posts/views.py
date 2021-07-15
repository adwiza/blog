from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse

from posts.models import Post


class PostsListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    template = 'posts/list.html'


def json_list_published_posts(requests):
    posts = Post.objects.filter(status='published')
    1 / 0
    return JsonResponse(
        {
            'posts': [
                {
                    'title': p.title,
                    'slug': p.slug,
                    'id': p.id,
                    'published': p.when_published,
                    'category': p.category,
                }
                for p in posts
            ]
        }
    )
