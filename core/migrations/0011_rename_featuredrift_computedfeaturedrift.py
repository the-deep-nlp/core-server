# Generated by Django 4.1.7 on 2023-02-28 06:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0010_featuredrift"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="FeatureDrift",
            new_name="ComputedFeatureDrift",
        ),
    ]
