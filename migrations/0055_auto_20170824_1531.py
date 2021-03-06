# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-24 14:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0054_auto_20170824_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('picture_url', models.CharField(blank=True, max_length=200)),
                ('is_picture', models.BooleanField(default=False)),
                ('is_problem', models.BooleanField(default=False)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggest', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestions', to='customUser.School')),
            ],
        ),
        migrations.RemoveField(
            model_name='modifsuggest',
            name='SentTo',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='SentTo',
        ),
        migrations.DeleteModel(
            name='ModifSuggest',
        ),
        migrations.DeleteModel(
            name='Problem',
        ),
    ]
