# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0016_auto_20170815_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='owner',
        ),
        migrations.AlterField(
            model_name='status',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='customUser.Comment'),
        ),
    ]
