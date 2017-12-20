from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from markdown import markdown
from django_markdown.models import MarkdownField

from blog.utils.slugify import unique_slugify


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images")
    post = models.ForeignKey('Post')

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

    @property
    def markdown_to_html(self):
        image_ref = ""

        for image in self.images.all():
            image_url = image.image.url

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
    post = models.ForeignKey('blog.Post')

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Hit(models.Model):
    """
    PageCounter: Used to count the number of hits in the site
    """
    created_ts = models.DateTimeField('created', auto_now_add=True)
    updated_ts = models.DateTimeField('updated', auto_now=True)
    ip = models.GenericIPAddressField()
    count = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return str(self.ip) + '-' + str(self.count)
