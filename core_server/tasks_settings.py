from celery.schedules import crontab
import core.tasks  # noqa

CELERY_BEAT_SCHEDULE = {
    "fetch_deep_data": {
        "task": "core.tasks.get_data.fetch_deep_data",
        "schedule": crontab(minute="0", hour="0"),  # every day
    },
}
