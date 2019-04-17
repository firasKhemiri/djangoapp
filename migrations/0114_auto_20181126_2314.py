# Generated by Django 2.0.1 on 2018-11-26 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customUser', '0113_auto_20181126_0300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='school',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='department',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='school',
        ),
        migrations.RemoveField(
            model_name='department',
            name='school',
        ),
        migrations.RemoveField(
            model_name='notes',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='otherdocs',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='pending',
            name='school',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='suggest',
            name='school',
        ),
        migrations.RemoveField(
            model_name='user',
            name='belongsTo',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.AddField(
            model_name='branch',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep_branches', to='customUser.Department'),
        ),
        migrations.AddField(
            model_name='classe',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_classes', to='customUser.Branch'),
        ),
    ]
