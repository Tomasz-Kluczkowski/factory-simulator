FROM python:3.9
LABEL maintainer="Tomasz-Kluczkowski@github.com"

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
