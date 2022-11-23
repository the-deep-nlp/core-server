from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "fetch_deep_data": {
        "task": "core.tasks.fetch_deep_data",
        "schedule": crontab(minute="0", hour="0"),  # every day at 12:00 AM
    },
    "create_indices": {
        "task": "deduplication.tasks.create_indices",
        "schedule": crontab(minute="0", hour="2"),  # every day at 02:00 AM
    },
}
