# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-04 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0090_event_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='departement',
        ),
    ]