# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0078_auto_20170927_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending',
            name='department',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep', to='customUser.Department'),
        ),
    ]
