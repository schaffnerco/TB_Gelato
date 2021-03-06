# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0014_categorie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='glace',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Image'),
        ),
    ]
