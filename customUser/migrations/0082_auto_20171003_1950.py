# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-03 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0081_auto_20171001_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_beg',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(),
        ),
    ]
