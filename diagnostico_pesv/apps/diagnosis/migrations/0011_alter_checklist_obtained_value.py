# Generated by Django 5.0.6 on 2024-07-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0010_checklist_is_articuled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='obtained_value',
            field=models.FloatField(default=0),
        ),
    ]
