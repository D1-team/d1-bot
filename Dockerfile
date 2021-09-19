FROM python:3.8-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
#RUN /opt/venv/bin/python3 -m pip install --upgrade pip
# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
