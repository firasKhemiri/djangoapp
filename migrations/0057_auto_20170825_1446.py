# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-25 13:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0056_auto_20170825_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classe',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='classe', to='customUser.School'),
        ),
        migrations.AlterField(
            model_name='department',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departement', to='customUser.School'),
        ),
    ]