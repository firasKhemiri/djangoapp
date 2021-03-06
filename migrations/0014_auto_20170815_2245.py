# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0013_auto_20170815_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='comments',
            field=models.ManyToManyField(related_name='comments', to='customUser.Comment'),
        ),
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
