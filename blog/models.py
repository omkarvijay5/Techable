from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Blog(models.Model):
    """
    Each user can create his own blog through admin.
    User can create only one blog of their own
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)

    def __unicode__(self):
        return self.title