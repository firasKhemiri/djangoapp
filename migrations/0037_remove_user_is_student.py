# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-18 00:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0036_auto_20170818_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
    ]