# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160624_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='datestr',
            field=models.CharField(default='June 28, 2016', max_length=127),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datestr',
            field=models.CharField(default='June 28, 2016 8:32 AM PST', max_length=127),
        ),
    ]
