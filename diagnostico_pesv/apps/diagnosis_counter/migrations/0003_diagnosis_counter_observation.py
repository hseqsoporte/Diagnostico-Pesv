# Generated by Django 5.1 on 2024-08-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis_counter', '0002_diagnosis_counter_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis_counter',
            name='observation',
            field=models.TextField(default=None, null=True),
        ),
    ]
