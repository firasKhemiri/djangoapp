# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-03 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0089_auto_20171003_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
