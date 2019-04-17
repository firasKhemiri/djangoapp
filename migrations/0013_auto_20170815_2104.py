# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0012_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='status',
            name='comments',
            field=models.ManyToManyField(related_name='comments', to='customUser.Comment'),
        ),
    ]