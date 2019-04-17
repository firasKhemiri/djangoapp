# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-15 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0022_auto_20170815_2323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bucketlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='status',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='customUser.Comment'),
        ),
    ]