import requests
import csv

from celery import Celery
#from extensions import Celery

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

celery = Celery("tasks", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task
def get_satellites():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=visual&FORMAT=json"
    data = requests.get(url)
    return data
