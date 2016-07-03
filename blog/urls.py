"""blog URL Configuration

The `urlpatterns` list routes URLs to blog views.
"""
from django.conf.urls import url, patterns

from blog.views import dashboard

urlpatterns = patterns(
    '',
    url(r'^$', dashboard, name='dashboard'),
)
