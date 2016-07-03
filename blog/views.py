from django.shortcuts import render, get_object_or_404


# Create your views here.
from blog.models import Post


def dashboard(request):
    return render(request, 'blog/dashboard.html', {})

def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
