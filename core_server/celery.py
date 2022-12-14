import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_server.settings")

app = Celery("core_server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
