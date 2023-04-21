import environ


env = environ.Env(
    DEBUG=(bool, False),
    IS_MOCKSERVER=(bool, False),
    ENVIRONMENT=str,
    DJANGO_SECRET_KEY=str,
    ALLOWED_HOSTS=list,
    ENDPOINT_NAME=(str, "http://localhost"),
    CSRF_TRUSTED_ORIGINS=list,
    USE_S3=(bool, True),
    CALLBACK_MAX_RETRIES_LIMIT=(int, 5),
    # Celery
    CELERY_BROKER_URL=str,
    CELERY_RESULT_BACKEND=str,
    # CRON
    CRON_DEEP_FETCH_MINUTE=str,
    CRON_DEEP_FETCH_HOUR=str,
    CRON_CREATE_INDICES_MINUTE=str,
    CRON_CREATE_INDICES_HOUR=str,
    # DB
    POSTGRES_DB=str,
    POSTGRES_USER=str,
    POSTGRES_PASSWORD=str,
    POSTGRES_HOSTNAME=str,
    POSTGRES_PORT=int,
    DEEP_DB_PASSWORD=str,
    DEEP_DB_NAME=str,
    DEEP_DB_USER=str,
    DEEP_DB_PORT=int,
    DEEP_DB_HOST=str,

    # SENTRY
    SENTRY_DSN=str,
    SENTRY_TRACES_SAMPLE_RATE=(float, 0.2),

    # AWS
    AWS_ACCESS_KEY_ID=(str, None),
    AWS_SECRET_ACCESS_KEY=(str, None),
    AWS_S3_ACCESS_KEY_ID=(str, None),
    AWS_S3_SECRET_ACCESS_KEY=(str, None),
    AWS_S3_BUCKET_NAME=(str, None),
    AWS_S3_REGION_NAME=(str, None),
)
