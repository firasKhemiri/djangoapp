# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-24 11:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0052_auto_20170823_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='students',
            field=models.ManyToManyField(related_name='notifications', to=settings.AUTH_USER_MODEL, verbose_name='Students'),
        ),
    ]
