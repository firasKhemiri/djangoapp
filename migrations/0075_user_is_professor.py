# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-25 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0074_auto_20170925_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_professor',
            field=models.BooleanField(default=False),
        ),
    ]