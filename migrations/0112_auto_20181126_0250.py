# Generated by Django 2.0.1 on 2018-11-26 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0111_auto_20181126_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pending',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep', to='customUser.Department'),
        ),
    ]