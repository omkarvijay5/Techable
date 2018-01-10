# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import base.storage


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=base.storage.upload_image),
        ),
    ]
