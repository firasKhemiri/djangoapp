# Generated by Django 2.0.1 on 2018-11-26 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0116_auto_20181127_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classe',
            name='year',
        ),
    ]
