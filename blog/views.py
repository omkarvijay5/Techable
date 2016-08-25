from django.shortcuts import render


# Create your views here.
from blog.services import get_post_details, get_posts_categories_tags


def dashboard(request):
    categories, posts, tags = get_posts_categories_tags()
    context = {'categories': categories, 'tags': tags, 'posts': posts}
    return render(request, 'blog/dashboard.html', context)


def post_detail(request, post_slug):
    post, categories, posts, tags = get_post_details(post_slug)
    context = {'post': post, 'categories': categories, 'tags': set(tags), 'posts': posts}
    return render(request, 'blog/post_detail.html', context)

def page_counter(request):
    pageCounter=PageCounter.objects.all()[0] 
    pageCounter.count+=1
    pageCounter.save()
    context = {'page_counter': pageCounter}
    return render(request,'blog/dashboard.html',context)
