# Generated by Django 2.0.1 on 2018-01-27 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0107_notification_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
