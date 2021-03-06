# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-01 14:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0080_auto_20170929_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='cours_comments', to='customUser.Commentaire'),
        ),
        migrations.AddField(
            model_name='courses',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='cours_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
