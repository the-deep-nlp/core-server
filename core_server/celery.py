import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_server.settings")

app = Celery("core_server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'run-nlp-scripts': {
#         'task': 'core.tasks.run_nlp_scripts',
#         # 'schedule': crontab(minute=0, hour=0),
#         'schedule': crontab(minute='*/15'),
#     },
# }