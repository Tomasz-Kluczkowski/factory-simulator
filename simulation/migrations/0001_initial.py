# Generated by Django 2.2.8 on 2021-01-24 13:53

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Simulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('start', models.DateTimeField()),
                ('stop', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efficiency', models.DecimalField(decimal_places=2, max_digits=4)),
                ('simulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Simulation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FactoryConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materials', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), size=None)),
                ('product_code', models.CharField(max_length=30)),
                ('empty_code', models.CharField(max_length=30)),
                ('number_of_simulation_steps', models.PositiveIntegerField()),
                ('number_of_conveyor_belt_slots', models.PositiveSmallIntegerField()),
                ('number_of_worker_pairs', models.PositiveSmallIntegerField()),
                ('pickup_time', models.PositiveSmallIntegerField()),
                ('drop_time', models.PositiveSmallIntegerField()),
                ('build_time', models.PositiveSmallIntegerField()),
                ('simulation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simulation.Simulation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
