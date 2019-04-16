# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-29 19:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0079_auto_20170927_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_class',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_depp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifs', to=settings.AUTH_USER_MODEL),
        ),
    ]