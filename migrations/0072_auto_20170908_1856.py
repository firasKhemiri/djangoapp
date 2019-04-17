# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-08 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0071_auto_20170907_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='pic_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
