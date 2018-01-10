# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import base.storage
import django_markdown.models
import django.contrib.postgres.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_ts', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated_ts', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('ip', models.GenericIPAddressField()),
                ('count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=base.storage.upload_image)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('posted_on', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('tags', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=255), blank=True)),
                ('body', django_markdown.models.MarkdownField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
