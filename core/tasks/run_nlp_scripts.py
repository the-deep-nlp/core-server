from celery import shared_task
from datetime import datetime


@shared_task
def run_nlp_scripts():
    # Perform some action here
    print("Task executed at", datetime.now())
