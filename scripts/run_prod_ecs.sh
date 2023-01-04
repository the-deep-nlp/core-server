#!/bin/bash

wait_cmd="/code/scripts/wait-for-it.sh $POSTGRES_HOSTNAME:$POSTGRES_PORT"

# Run celery and beat in background
$wait_cmd && celery -A core_server worker -l info &
$wait_cmd && celery -A core_server beat -l info &

# Run server
$wait_cmd && \
        python manage.py migrate && \
        python manage.py collectstatic --noinput && \
        gunicorn -w 4 -b 0.0.0.0:8000 core_server.wsgi:application
