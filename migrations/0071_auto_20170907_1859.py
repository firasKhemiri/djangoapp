# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-07 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0070_remove_poststat_is_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentaire',
            old_name='text',
            new_name='comment',
        ),
    ]
