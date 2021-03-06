# Generated by Django 2.0.1 on 2018-11-29 15:04

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0124_auto_20181129_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='xCoord',
            field=models.DecimalField(decimal_places=20, default=Decimal('0'), max_digits=20),
        ),
        migrations.AddField(
            model_name='event',
            name='yCoord',
            field=models.DecimalField(decimal_places=20, default=Decimal('0'), max_digits=20),
        ),
    ]
