# Generated by Django 5.0.6 on 2024-07-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0002_user_cedula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cedula',
            field=models.CharField(blank=True, default=23812, max_length=10, null=None, unique=True),
            preserve_default=False,
        ),
    ]
