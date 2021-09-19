FROM python:3.9-slim

RUN apt-get update && apt-get -y install black
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
