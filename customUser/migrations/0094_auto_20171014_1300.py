# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-14 12:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0093_auto_20171004_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='who_is_followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, null=True, related_name='who_follows', to=settings.AUTH_USER_MODEL),
        ),
    ]
