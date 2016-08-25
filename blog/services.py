from django.shortcuts import get_object_or_404

from blog.models import Category, Post, PageCounter


def get_tags(posts):
    return {tag for post in posts for tag in post.tags}


def get_post_details(post_slug):
    post = get_object_or_404(Post.objects.select_related('author').prefetch_related('images'), slug=post_slug)

    # calculate all tags for all posts
    categories = Category.objects.all().prefetch_related('posts')
    posts = Post.objects.all().select_related('author')
    tags = get_tags(posts)
    return post, categories, posts, tags


def get_posts_categories_tags():
    categories = Category.objects.all()
    posts = Post.objects.all().select_related('author').prefetch_related('images')
    tags = get_tags(posts)
    return categories, posts, tags

def get_page_counter():
    page_count = PageCounter.objects.all()
    return page_count