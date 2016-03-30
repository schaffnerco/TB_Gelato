# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0003_auto_20160329_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congelateur',
            name='code',
            field=models.CharField(max_length=15, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='tiroir',
            name='code',
            field=models.CharField(max_length=15, unique=True, verbose_name='Code'),
        ),
    ]
