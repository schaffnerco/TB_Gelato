# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0005_congelateur_nombredebac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congelateur',
            name='nombreDeBac',
            field=models.IntegerField(blank=True, verbose_name='Nombre de bacs'),
        ),
    ]