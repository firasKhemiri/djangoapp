# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-11 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0072_auto_20170908_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(max_length=6255),
        ),
    ]
