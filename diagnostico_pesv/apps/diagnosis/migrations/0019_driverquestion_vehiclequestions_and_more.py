# Generated by Django 5.0.6 on 2024-08-06 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0018_diagnosis_schedule_diagnosis_sequence'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('name', models.CharField(max_length=255, null=None, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnosis.driverquestion'),
        ),
        migrations.AlterField(
            model_name='fleet',
            name='vehicle_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnosis.vehiclequestions'),
        ),
    ]
