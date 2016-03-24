from django.contrib import admin
from blog.models import Blog, Category, Post

from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget


class BaseAdminMixin(object):
    exclude = ('slug',)


@admin.register(Blog)
class BlogAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(BaseAdminMixin, admin.ModelAdmin):
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}
