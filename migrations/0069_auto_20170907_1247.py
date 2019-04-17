# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 11:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0068_user_is_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='poststat',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to=settings.AUTH_USER_MODEL),
        ),
    ]