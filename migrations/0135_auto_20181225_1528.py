# Generated by Django 2.1.4 on 2018-12-25 14:28

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0134_auto_20181225_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='lat',
            field=models.DecimalField(decimal_places=8, default=Decimal('0'), max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='lng',
            field=models.DecimalField(decimal_places=8, default=Decimal('0'), max_digits=10),
        ),
    ]