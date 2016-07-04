from collections import defaultdict

from django.shortcuts import render, get_object_or_404


# Create your views here.
from blog.models import Post, Category


def dashboard(request):
    return render(request, 'blog/dashboard.html', {})


def post_detail(request, post_slug):
    post = get_object_or_404(Post.objects.select_related('author'), slug=post_slug)
    categories = Category.objects.all().prefetch_related('posts')
    posts = Post.objects.filter(category__in=categories).select_related('author')

    # calculate all tags for all posts
    tags = []
    for post in posts:
        tags.extend(post.tags)
    context = {'post': post, 'categories': categories, 'tags': tags, 'posts': posts}
    return render(request, 'blog/post_detail.html', context)
