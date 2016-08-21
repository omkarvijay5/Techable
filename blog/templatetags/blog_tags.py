import re

from django import template
from django.conf import settings


register = template.Library()

@register.assignment_tag
def get_post_img_url(post):
    post_images = post.images.all()
    if post_images:
        return post_images[0].image.url
    return settings.STATIC_URL + "images/slider-wallpaper-colorlib-750x410.png"

@register.filter
def post_desc(post):
    return re.sub("(<[^>]+>)", '', post.markdown_to_html)[:400]
