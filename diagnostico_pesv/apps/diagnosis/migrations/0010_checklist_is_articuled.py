# Generated by Django 5.0.6 on 2024-07-24 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0009_remove_diagnosis_questions_cycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklist',
            name='is_articuled',
            field=models.BooleanField(default=True),
        ),
    ]
