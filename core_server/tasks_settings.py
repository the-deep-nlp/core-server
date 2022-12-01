from celery.schedules import crontab
from .env import env

CELERY_BEAT_SCHEDULE = {
    "fetch_deep_data": {
        "task": "core.tasks.get_data.fetch_deep_data",
        "schedule": crontab(
            minute=env("CRON_DEEP_FETCH_MINUTE"),
            hour=env("CRON_DEEP_FETCH_HOUR"),
        ),  # defaults to every day at 12:00 AM
    },
    "create_indices": {
        "task": "deduplication.tasks.indexing.create_indices",
        "schedule": crontab(
            minute=env("CRON_CREATE_INDICES_MINUTE"),
            hour=env("CRON_CREATE_INDICES_HOUR"),
        ),  # defaults to every day at 02:00 AM
    },
}
