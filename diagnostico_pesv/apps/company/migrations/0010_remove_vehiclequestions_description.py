# Generated by Django 5.0.6 on 2024-07-10 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_vehiclequestions_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclequestions',
            name='description',
        ),
    ]
