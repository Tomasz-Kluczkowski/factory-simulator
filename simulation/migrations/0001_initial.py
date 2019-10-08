# Generated by Django 2.2.5 on 2019-10-08 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='simulation.Receiver')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('received_at', models.DateTimeField(blank=True, null=True)),
                ('feeder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='components', to='simulation.Feeder')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='components', to='simulation.Receiver')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
