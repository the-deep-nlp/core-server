# Generated by Django 4.1.7 on 2023-05-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_nlprequest_last_process_attempted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nlprequest',
            name='type',
            field=models.CharField(choices=[('ngrams', 'Ngrams'), ('topicmodel', 'Topicmodel'), ('summarization', 'Summarization'), ('summarization-v2', 'Summarization-V2'), ('geolocation', 'Geolocation'), ('tags-mapping', 'Tags Mapping'), ('entry-classification', 'Entry Classification'), ('text-extraction', 'Text Extraction')], max_length=20),
        ),
    ]
