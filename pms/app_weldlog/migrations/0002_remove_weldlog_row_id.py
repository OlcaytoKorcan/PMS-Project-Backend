# Generated by Django 4.0.4 on 2022-11-20 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_weldlog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weldlog',
            name='row_id',
        ),
    ]
