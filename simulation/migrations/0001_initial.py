# Generated by Django 2.2.5 on 2020-02-01 20:47

import django.contrib.postgres.fields
from django.db import migrations, models
import simulation.models.factory_config


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FactoryConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_component_names', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), default=simulation.models.factory_config.get_default_required_names, size=None)),
                ('product_code', models.CharField(default='P', max_length=30)),
                ('empty_code', models.CharField(default='E', max_length=30)),
                ('number_of_simulation_steps', models.PositiveIntegerField(default=10)),
                ('number_of_conveyor_belt_slots', models.PositiveSmallIntegerField(default=3)),
                ('number_of_worker_pairs', models.PositiveSmallIntegerField(default=3)),
                ('pick_up_time', models.PositiveSmallIntegerField(default=1)),
                ('drop_time', models.PositiveSmallIntegerField(default=1)),
                ('build_time', models.PositiveSmallIntegerField(default=4)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
