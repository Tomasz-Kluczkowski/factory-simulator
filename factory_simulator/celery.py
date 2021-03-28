import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'factory_simulator.settings')

celery_app = Celery('factory_simulator')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
celery_app.autodiscover_tasks()


def get_celery_broker_url(
    broker: str,
    broker_username: str,
    broker_password: str,
    broker_host: str,
    broker_port: str,
    broker_virtual_host: str
) -> str:
    return f'{broker}://{broker_username}:{broker_password}@{broker_host}:{broker_port}/{broker_virtual_host}'


def get_celery_result_backend_url(
    result_backend: str,
    result_backend_host: str,
    result_backend_db: str,
) -> str:
    return f'{result_backend}://{result_backend_host}/{result_backend_db}'
