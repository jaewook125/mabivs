# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170710_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userid',
            field=models.CharField(max_length=20),
        ),
    ]
