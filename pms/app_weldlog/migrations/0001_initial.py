# Generated by Django 4.0.4 on 2022-11-20 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weldlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_id', models.IntegerField(blank=True, null=True)),
                ('line', models.CharField(max_length=100)),
                ('isometry', models.CharField(max_length=100)),
                ('spool', models.CharField(max_length=100)),
                ('joint', models.CharField(max_length=100)),
                ('dia', models.PositiveSmallIntegerField()),
                ('mat1', models.CharField(max_length=100)),
                ('p1', models.PositiveSmallIntegerField()),
                ('mat2', models.CharField(max_length=100)),
                ('p2', models.PositiveSmallIntegerField()),
                ('fitupdate', models.DateField(blank=True, null=True)),
                ('fitupresult', models.CharField(blank=True, max_length=20)),
                ('weldclass', models.CharField(max_length=10)),
                ('pwht', models.CharField(choices=[('Y', 'Y'), ('N', 'N')], max_length=100)),
                ('wps', models.CharField(blank=True, max_length=10)),
                ('location', models.CharField(max_length=10)),
                ('weldtype', models.CharField(max_length=100)),
                ('welder', models.CharField(blank=True, max_length=100)),
                ('vtdate', models.DateField(blank=True, null=True)),
                ('vtreport', models.CharField(blank=True, max_length=100)),
                ('pwhtdate', models.DateField(blank=True, null=True)),
                ('pwhtreport', models.CharField(blank=True, max_length=100)),
                ('rtdate', models.DateField(blank=True, null=True)),
                ('rtreportno', models.CharField(blank=True, max_length=100)),
                ('rtresult', models.CharField(blank=True, choices=[('Accept', 'Accept'), ('Reject', 'Reject')], max_length=100)),
                ('penalty', models.CharField(blank=True, max_length=100)),
                ('tpno', models.CharField(blank=True, max_length=100)),
                ('cancel', models.CharField(blank=True, max_length=100)),
                ('rtrate', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('pwhtrate', models.PositiveSmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'weldlog_table',
            },
        ),
    ]
