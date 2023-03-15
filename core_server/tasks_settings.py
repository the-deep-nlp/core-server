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
    "calculate_model_metrics": {
        "task": "core.tasks.model_monitoring.calculate_model_metrics",
        "schedule": crontab(
            hour="0",
            minute="0",
        ),  # do it every day at 12 am
    },
    "fetch_new_projects": {
        "task": "core.tasks.get_data.fetch_new_projects",
        "schedule": crontab(
            hour="*/12",  # Do it every 12 hours
            minute="0",
        ),
    }
}
