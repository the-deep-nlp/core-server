# Generated by Django 4.1.7 on 2023-03-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_allprojectperfmetrics_categorywisematchratios_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tofetchproject',
            name='active_status',
            field=models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=20),
        ),
    ]
