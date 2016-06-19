from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.postgres.fields import ArrayField
import markdown
from django_markdown.models import MarkdownField

from blog_utils.slugify import unique_slugify


class Blog(models.Model):
    """
    only one blog can be created
    slug: generates slug automatically while saving object
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        override save method to prevent creating more than one blog
        """
        if Blog.objects.count() == 1 and self.id is None:
            raise PermissionDenied("you cannot create more than one blog")
        elif self.id is None:
            unique_slugify(self, self.title)
        super(Blog, self).save(*args, **kwargs)


def markdown_to_html(markdownText, images):
    image_ref = ""

    for image in images:
        image_url = settings.MEDIA_URL + image.image.url
        image_ref = "%s\n[%s]: %s" % (image_ref, image, image_url)

    md = "%s\n%s" % (markdownText, image_ref)
    html = markdown.markdown(md)

    return html


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images")

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """
    Different Authors can post their own articles in the blog
    posted_on: defines when post was being posted
    is_published: True when post is live. When False it will be visible only
    for the author. Author can view how post looks like and make approval for
    publishing
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    posted_on = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_published = models.BooleanField(default=False)
    tags = ArrayField(models.CharField(max_length=255), null=True, blank=True)
    body = MarkdownField()
    images = models.ManyToManyField(Image, blank=True)

    def __unicode__(self):
        return self.title

    def body_html(self):
        return markdown_to_html(self.body, self.images.all())

    def save(self, *args, **kwargs):
        if self.id is None:
            unique_slugify(self, self.title)
        super(Post, self).save(*args, **kwargs)
