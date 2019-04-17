# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 21:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0015_auto_20170815_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='customUser.Comment'),
        ),
        migrations.AlterField(
            model_name='status',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]