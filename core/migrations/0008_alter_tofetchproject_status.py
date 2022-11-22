# Generated by Django 4.1.3 on 2022-11-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_lead_text_extract'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tofetchproject',
            name='status',
            field=models.CharField(choices=[('not_fetched', 'Not Fetched'), ('fetching', 'Fetching'), ('fetched', 'Fetched'), ('errored', 'Errored'), ('not_found', 'Not Found')], default='not_fetched', max_length=20),
        ),
    ]
