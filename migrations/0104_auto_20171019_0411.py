# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-19 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0103_auto_20171019_0235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('file_path', models.CharField(max_length=255)),
                ('creator', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school_notes', to='customUser.School')),
            ],
        ),
        migrations.CreateModel(
            name='Other_docs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('file_path', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_docs', to='customUser.School')),
            ],
        ),
        migrations.AlterField(
            model_name='schedule',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='school_schedules', to='customUser.School'),
        ),
    ]
