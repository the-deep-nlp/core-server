# Generated by Django 4.1.7 on 2023-04-12 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_module', '0004_remove_analysismodulerequest_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysismodulerequest',
            name='result_s3_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]
