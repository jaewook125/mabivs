# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('w', 'Wolf'), ('m', 'Mandolin'), ('h', 'Harf'), ('L', 'Lute')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
