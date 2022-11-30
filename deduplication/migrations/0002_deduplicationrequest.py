# Generated by Django 4.1.3 on 2022-11-30 05:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deduplication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeduplicationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('calculated', 'Calculated'), ('responded', 'Responded')], default='pending', max_length=15)),
                ('project_id', models.IntegerField()),
                ('lead_id', models.IntegerField()),
                ('callback_url', models.TextField()),
                ('text_extract', models.TextField()),
                ('has_errored', models.BooleanField(default=False)),
                ('error', models.TextField(blank=True, null=True)),
                ('result', models.JSONField(default=dict)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('project_id', 'lead_id')},
            },
        ),
    ]
