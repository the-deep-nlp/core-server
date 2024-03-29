# Generated by Django 4.2.3 on 2023-07-21 06:39

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_remove_nlprequest_result_s3_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='excerpt_en',
            new_name='excerpt',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='af_exportable_data',
        ),
        migrations.AddField(
            model_name='entry',
            name='nlp_mapping',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='entry',
            name='nlp_tags',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='affected_groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='age',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='gender',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='sectors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='severity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='specific_needs_groups',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='subpillars_1d',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='classificationpredictions',
            name='subpillars_2d',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=None),
        ),
    ]
