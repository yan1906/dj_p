# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20171021_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Comment text'),
        ),
    ]
