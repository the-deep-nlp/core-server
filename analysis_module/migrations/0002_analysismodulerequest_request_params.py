# Generated by Django 4.1.7 on 2023-03-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysismodulerequest',
            name='request_params',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
