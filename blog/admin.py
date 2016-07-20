from django.contrib import admin
from django.forms import ValidationError, ModelForm
from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget
from django_markdown.admin import MarkdownModelAdmin

from blog.models import Post, Image, Category


class BaseAdminMixin(object):
    exclude = ('slug',)


@admin.register(Image)
class ImageAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass


class CategoryInlineAdmin(admin.TabularInline):
    model = Category.posts.through
    extra = 1


@admin.register(Post)
class PostAdmin(MarkdownModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
