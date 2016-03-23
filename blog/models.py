from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


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
