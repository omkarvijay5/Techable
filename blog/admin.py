from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from blog.models import Post, Image, Category, Hit


class BaseAdminMixin(object):
    exclude = ('slug',)


@admin.register(Image)
class ImageAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass


class CategoryInlineAdmin(admin.TabularInline):
    model = Category
    extra = 1


@admin.register(Post)
class PostAdmin(MarkdownModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Hit)
class HitCountAdmin(admin.ModelAdmin):
    pass
