# Generated by Django 2.1.4 on 2018-12-25 13:11

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0130_auto_20181213_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=15, default=Decimal('0'), max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=15, default=Decimal('0'), max_digits=20, null=True),
        ),
    ]
