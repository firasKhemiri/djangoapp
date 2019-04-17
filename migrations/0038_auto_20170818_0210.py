# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-18 01:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0037_remove_user_is_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('picture_url', models.CharField(blank=True, max_length=200)),
                ('is_picture', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='school',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='school',
            name='date_modified',
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='who_is_followed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='who_follows', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='problem',
            name='SentTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Problem_school', to='customUser.School'),
        ),
        migrations.AddField(
            model_name='notification',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notif', to='customUser.School'),
        ),
    ]
