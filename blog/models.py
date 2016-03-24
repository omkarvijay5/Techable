from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

from django_markdown.models import MarkdownField


class Blog(models.Model):
    """
    Each user can create his own blog through admin.
    User can create only one blog of their own
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        user = self.user
        if self.id is None:
            slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class Category(models.Model):
    """
    category model which defines the category of a post.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        user = self.user
        if self.id is None:
            slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    posted_on = models.DateTimeField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    is_published = models.BooleanField(default=False)
    text = MarkdownField()

    def __unicode__(self):
        return self.title


    def save(self, *args, **kwargs):
        user = self.user
        if self.id is None:
            slugify(self.title)
        super(Post, self).save(*args, **kwargs)
