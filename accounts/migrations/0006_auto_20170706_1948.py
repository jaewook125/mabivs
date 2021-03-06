# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170706_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='race',
            field=models.CharField(choices=[('인간', '인간'), ('엘프', '엘프'), ('자이언트', '자이언트')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='server',
            field=models.CharField(choices=[('울프', '울프'), ('만돌린', '만돌린'), ('하프', '하프'), ('류트', '류트')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.CharField(choices=[('근접 전투', '근접 전투'), ('랜스', '랜스'), ('궁술', '궁술'), ('마법', '마법'), ('격투술', '격투술'), ('연금술', '연금술'), ('기타', '기타')], max_length=1),
        ),
    ]
