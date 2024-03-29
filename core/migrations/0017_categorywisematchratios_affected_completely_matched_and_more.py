# Generated by Django 4.2.3 on 2023-08-11 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_allprojectperfmetrics_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorywisematchratios',
            name='affected_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='affected_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='affected_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='age_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='age_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='age_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='displaced_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='displaced_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='displaced_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='gender_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='gender_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='gender_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='non_displaced_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='non_displaced_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='non_displaced_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='pillars_1d_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='pillars_1d_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='pillars_1d_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='pillars_2d_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='pillars_2d_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='pillars_2d_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='severity_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='severity_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='severity_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='specific_needs_groups_completely_matched',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='specific_needs_groups_missing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorywisematchratios',
            name='specific_needs_groups_wrong',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='affected_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='affected_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='affected_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='age_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='age_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='age_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='displaced_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='displaced_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='displaced_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='gender_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='gender_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='gender_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='non_displaced_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='non_displaced_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='non_displaced_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='pillars_1d_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='pillars_1d_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='pillars_1d_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='pillars_2d_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='pillars_2d_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='pillars_2d_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='severity_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='severity_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='severity_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='specific_needs_groups_completely_matched_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='specific_needs_groups_missing_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectwisematchratios',
            name='specific_needs_groups_wrong_mean',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
