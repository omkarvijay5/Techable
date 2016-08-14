from django.shortcuts import get_object_or_404

from blog.models import Category, Post


def get_post_details(post_slug):
    post = get_object_or_404(Post.objects.select_related('author').prefetch_related('images'), slug=post_slug)

    # calculate all tags for all posts
    categories = Category.objects.all().prefetch_related('posts')
    posts = Post.objects.filter(category__in=categories).select_related('author')
    tags = []
    for blog_post in posts:
        tags.extend(blog_post.tags)
    return post, categories, posts, tags
