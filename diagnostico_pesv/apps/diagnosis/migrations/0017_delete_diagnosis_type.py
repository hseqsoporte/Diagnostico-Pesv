# Generated by Django 5.0.6 on 2024-07-31 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0016_rename_checlist_requirement_checklist_requirement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Diagnosis_Type',
        ),
    ]
