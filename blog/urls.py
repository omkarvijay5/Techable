"""blog URL Configuration

The `urlpatterns` list routes URLs to blog views.
"""
from django.conf.urls import url

from blog.views import dashboard, post_detail

urlpatterns = [
    url(r'^$', dashboard, name='dashboard'),

    # post detail
    url(r'^post-detail/(?P<post_slug>[\w-]+)/$', post_detail, name='post_detail'),
]
