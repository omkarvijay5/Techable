from django import template
from django.conf import settings
from django.contrib.sites.models import Site


register = template.Library()

@register.assignment_tag
def get_meta_img_url(post):
    post_images = post.images.all()
    current_site = Site.objects.get_current()
    domain_name = current_site.domain
    if post_images:
        return 'http://' + domain_name + post_images[0].image.url
    return 'http://' + domain_name + settings.STATIC_URL + "/images/slider-wallpaper-colorlib-750x410.png"
