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
    USE_NEW_SUMMARIZATION=(bool, True),
    CALLBACK_MAX_RETRIES_LIMIT=(int, 5),
    ECS_REQUESTS_BATCH_SIZE=(int, 20),
    MAX_NLP_PROCESSING_ATTEMPTS=(int, 3),
    # Celery
    CELERY_BROKER_URL=str,
    CELERY_RESULT_BACKEND=str,
    # CRON
    CRON_DEEP_FETCH_MINUTE=str,
    CRON_DEEP_FETCH_HOUR=str,
    CRON_CREATE_INDICES_MINUTE=str,
    CRON_CREATE_INDICES_HOUR=str,
    CRON_FAILED_CALLBACK_SCHEDULE=(str, "*/15"),
    CRON_RESEND_ECS_REQUEST_MINUTES=(int, 15),
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
    FETCH_DEEP_PROJECTS_AFTER=(str, "2021-01-01"),

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

    # ECS
    CLASSIFICATION_MODEL_ENDPOINT=(str, "main-model-cpu"),
    SUMMARIZATION_V3_ECS_ENDPOINT=(str, None),
    TEXTEXTRACTION_ECS_ENDPOINT=(str, None),

    # MODEL INFO
    CLASSIFICATION_MODEL_ID=str,
    CLASSIFICATION_MODEL_VERSION=str,
    GEOLOCATION_MODEL_ID=str,
    GEOLOCATION_MODEL_VERSION=str,
    RELIABILITY_MODEL_ID=str,
    RELIABILITY_MODEL_VERSION=str,

    # LLM 
    OPENAI_API_KEY=str,
    OPENAI_MAIN_MODEL=(str, "gpt-4o"),
    OPENAI_SMALL_MODEL=(str, "gpt-4o-mini"),
    BEDROCK_MAIN_MODEL=(str, "anthropic.claude-3-5-sonnet-20240620-v1:0"),
    BEDROCK_SMALL_MODEL=(str, "us.amazon.nova-micro-v1:0")
)
