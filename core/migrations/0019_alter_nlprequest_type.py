# Generated by Django 4.2.8 on 2024-01-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_nlprequest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nlprequest',
            name='type',
            field=models.CharField(choices=[('ngrams', 'Ngrams'), ('topicmodel', 'Topicmodel'), ('summarization', 'Summarization'), ('summarization-v3', 'Summarization-V3'), ('geolocation', 'Geolocation'), ('tags-mapping', 'Tags Mapping'), ('entry-classification', 'Entry Classification'), ('text-extraction', 'Text Extraction'), ('entry-extraction-classification', 'Entry Extraction Classification')], max_length=50),
        ),
    ]
