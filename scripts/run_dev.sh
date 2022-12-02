#!/bin/bash
run=${1:-server}
wait_cmd="/code/scripts/wait-for-it.sh $POSTGRES_HOSTNAME:$POSTGRES_PORT"

if [[ "$run" == "server" ]]; then
    $wait_cmd && \
        python manage.py migrate && \
        python manage.py runserver 0.0.0.0:8000
elif [[ "$run" == "celery" ]]; then
    $wait_cmd && celery -A core_server worker -l info
elif [[ "$run" == "beat" ]]; then
    $wait_cmd && celery -A core_server beat -l info
else
    echo "Wrong run command. Provide either 'server', 'celery' or 'beat'"
    exit 1
fi
