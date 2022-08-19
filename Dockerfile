FROM python:3.9-slim

RUN apt-get update
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

ENV DJANGO_SETTINGS_MODULE="config.settings"

WORKDIR /app

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
