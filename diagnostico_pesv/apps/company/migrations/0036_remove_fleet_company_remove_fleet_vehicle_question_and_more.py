# Generated by Django 5.0.6 on 2024-07-31 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0035_alter_ciiu_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fleet',
            name='company',
        ),
        migrations.RemoveField(
            model_name='fleet',
            name='vehicle_question',
        ),
        migrations.RemoveField(
            model_name='company',
            name='diagnosis',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='Fleet',
        ),
    ]