FROM python:3.7-buster
LABEL maintainer="Tomasz-Kluczkowski@github.com"

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "factory_simulator.wsgi:application"]