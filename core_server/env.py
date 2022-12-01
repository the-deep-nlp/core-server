import environ


env = environ.Env(
    DEBUG=(bool, False),
    DJANGO_SECRET_KEY=str,
    ALLOWED_HOSTS=(list, ['localhost']),

    # Celery
    CELERY_BROKER_URL=(str, "redis://redis:6379"),
    CELERY_RESULT_BACKEND=(str, "redis://redis:6379"),

    # CRON
    CRON_DEEP_FETCH_MINUTE=(str, "0"),
    CRON_DEEP_FETCH_HOUR=(str, "0"),
    CRON_CREATE_INDICES_MINUTE=(str, "0"),
    CRON_CREATE_INDICES_HOUR=(str, "2"),

    # DB
    POSTGRES_NAME=str,
    POSTGRES_USER=str,
    POSTGRES_PASSWORD=str,
    POSTGRES_HOST=str,
    POSTGRES_PORT=str,

    DEEP_DB_PASSWORD=str,
    DEEP_DB_NAME=str,
    DEEP_DB_USER=str,
    DEEP_DB_PORT=str,
    DEEP_DB_HOST=str,
)
