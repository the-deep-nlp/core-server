# Generated by Django 4.1.7 on 2023-03-13 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_allprojectperfmetrics_categorywisematchratios_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computedfeaturedrift',
            name='entry_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
