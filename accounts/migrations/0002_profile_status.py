# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('w', 'Wolf'), ('m', 'Mandolin'), ('h', 'Harf'), ('l', 'Lute')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
