# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-14 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0095_auto_20171014_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]