import environ


env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_SECRET_KEY=str,
    ALLOWED_HOSTS=list,
    # Celery
    CELERY_BROKER_URL=str,
    CELERY_RESULT_BACKEND=str,
    # CRON
    CRON_DEEP_FETCH_MINUTE=str,
    CRON_DEEP_FETCH_HOUR=str,
    CRON_CREATE_INDICES_MINUTE=str,
    CRON_CREATE_INDICES_HOUR=str,
    # DB
    POSTGRES_NAME=str,
    POSTGRES_USER=str,
    POSTGRES_PASSWORD=str,
    POSTGRES_HOST=str,
    POSTGRES_PORT=int,
    DEEP_DB_PASSWORD=str,
    DEEP_DB_NAME=str,
    DEEP_DB_USER=str,
    DEEP_DB_PORT=int,
    DEEP_DB_HOST=str,
)
