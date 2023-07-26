FROM python:3.10.6 as base

WORKDIR /code

COPY . /code/

RUN apt update -y \
    && apt install -y enchant-2 \
    && apt update -y \
    && pip install --upgrade --no-cache-dir pip pyyaml==5.3.1 poetry==1.2.2 pyenchant polars==0.18.6 pyarrow==12.0.0 \
    && poetry --version \
    # Configure to use system instead of virtualenvs
    && poetry config virtualenvs.create false \
    && poetry install --no-root \
    # Clean-up
    && pip uninstall -y poetry virtualenv-clone virtualenv \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*
