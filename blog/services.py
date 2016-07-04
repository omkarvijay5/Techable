from django.shortcuts import get_object_or_404

from blog.models import Category, Post


def get_post_details(post_slug):
    post = get_object_or_404(Post.objects.select_related('author'), slug=post_slug)
    categories = Category.objects.all().prefetch_related('posts')
    posts = Post.objects.filter(category__in=categories).select_related('author')

    # calculate all tags for all posts
    tags = []
    for post in posts:
        tags.extend(post.tags)
    return post, categories, posts, tags
