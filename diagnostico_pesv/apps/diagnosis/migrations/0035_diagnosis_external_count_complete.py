# Generated by Django 5.1 on 2024-09-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0034_diagnosis_corporate_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnosis',
            name='external_count_complete',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
