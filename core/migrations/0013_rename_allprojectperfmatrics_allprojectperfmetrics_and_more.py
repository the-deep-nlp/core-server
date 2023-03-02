# Generated by Django 4.1.7 on 2023-03-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_rename_url_classificationmodel_reference_train_data_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AllProjectPerfMatrics',
            new_name='AllProjectPerfMetrics',
        ),
        migrations.RenameModel(
            old_name='ProjectWisePerfMatrices',
            new_name='ProjectWisePerfMetrics',
        ),
        migrations.RenameModel(
            old_name='TagWisePerfMatrics',
            new_name='TagWisePerfMetrics',
        ),
        migrations.AddField(
            model_name='classificationmodel',
            name='defaults',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterUniqueTogether(
            name='classificationmodel',
            unique_together={('name', 'version', 'model_uri')},
        ),
        migrations.RemoveField(
            model_name='classificationmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='classificationmodel',
            name='reference_train_data',
        ),
    ]
