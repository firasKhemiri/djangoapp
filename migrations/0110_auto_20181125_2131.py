# Generated by Django 2.0.1 on 2018-11-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0109_auto_20180203_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_modified',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='poststat',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='poststat',
            name='date_modified',
            field=models.DateTimeField(),
        ),
    ]
