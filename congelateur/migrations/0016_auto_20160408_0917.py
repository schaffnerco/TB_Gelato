# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 07:17
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0015_auto_20160408_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glace',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/products'), upload_to='', verbose_name='Image'),
        ),
    ]
