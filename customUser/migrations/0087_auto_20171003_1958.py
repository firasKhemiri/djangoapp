# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-03 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0086_auto_20171003_1958'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Events',
        ),
    ]