# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
