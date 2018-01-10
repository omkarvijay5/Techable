from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.postgres.fields import ArrayField
from markdown import markdown
from django_markdown.models import MarkdownField

from blog.slugify import unique_slugify
from base.models import TimeStampedModel
from base.storage import upload_image


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_image)

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

    @property
    def markdown_to_html(self):
        image_ref = ""

        for image in self.images.all():
            image_url = settings.MEDIA_URL + image.image.url
            image_ref = "%s\n[%s]: %s" % (image_ref, image, image_url)

        md = "%s\n%s" % (self.body, image_ref)
        html = markdown(md)
        return html

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.id is None:
            unique_slugify(self, self.title)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    """
    Category: classification of posts in an area of expertise
    """
    name = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    posts = models.ManyToManyField('blog.Post', blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name
