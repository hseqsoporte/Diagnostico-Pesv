# Generated by Django 5.1 on 2024-08-20 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0039_remove_company_consultor'),
        ('corporate_group', '0002_corporate_name'),
        ('diagnosis', '0028_diagnosis_observation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='corporate',
            name='company',
        ),
        migrations.RemoveField(
            model_name='corporate',
            name='diagnosis',
        ),
        migrations.CreateModel(
            name='CorporateCompanyDiagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company')),
                ('corporate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='corporate_group.corporate')),
                ('diagnosis', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diagnosis.diagnosis')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
