# Generated by Django 4.1.1 on 2022-09-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weldlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weldlog',
            name='fitupdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='weldlog',
            name='pwhtdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='weldlog',
            name='rtdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='weldlog',
            name='vtdate',
            field=models.DateField(),
        ),
    ]
