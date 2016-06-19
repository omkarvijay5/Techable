from django.contrib import admin
from django.forms import ValidationError, ModelForm
from django_markdown.models import MarkdownField
from django_markdown.widgets import AdminMarkdownWidget

from blog.models import Blog, Post, Image


class BaseAdminMixin(object):
    exclude = ('slug',)


class BlogAdminForm(ModelForm):
    class Meta:
        model = Blog
        exclude = ()

    def clean(self):
        blogs = Blog.objects.all()
        if len(blogs) == 1:
            raise ValidationError('You cannot create more than one blog')
        return self.cleaned_data


@admin.register(Blog)
class BlogAdmin(BaseAdminMixin, admin.ModelAdmin):
    form = BlogAdminForm

@admin.register(Image)
class ImageAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(BaseAdminMixin, admin.ModelAdmin):
    formfield_overrides = {MarkdownField: {'widget': AdminMarkdownWidget}}
