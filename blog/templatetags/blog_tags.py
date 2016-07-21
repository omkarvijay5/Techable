from django import template
from django.conf import settings

register = template.Library()

@register.assignment_tag
def get_meta_img_url(post):
    post_images = post.images.all()
    if post_images:
        return settings.MEDIA_ROOT + post_images[0].image.name
    return settings.STATIC_ROOT + "/images/slider-wallpaper-colorlib-750x410.png"
