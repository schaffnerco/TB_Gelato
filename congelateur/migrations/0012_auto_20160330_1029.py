# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('congelateur', '0011_auto_20160330_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='sousCategorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='congelateur.Categorie', verbose_name='Catégorie'),
        ),
    ]
