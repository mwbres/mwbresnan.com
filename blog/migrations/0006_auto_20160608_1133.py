# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160608_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(blank=True, max_length=127, null=True),
        ),
    ]
