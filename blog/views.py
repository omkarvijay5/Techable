from django.shortcuts import render


# Create your views here.
from blog.services import get_post_details


def dashboard(request):
    return render(request, 'blog/dashboard.html', {})


def post_detail(request, post_slug):
    post, categories, posts, tags = get_post_details(post_slug)
    context = {'post': post, 'categories': categories, 'tags': set(tags), 'posts': posts}
    return render(request, 'blog/post_detail.html', context)
