# Generated by Django 4.1.7 on 2023-04-11 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_module', '0003_analysismodulerequest_error_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysismodulerequest',
            name='error',
        ),
    ]
