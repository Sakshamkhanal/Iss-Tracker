import requests
import csv
from celery import Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

celery = Celery('tasks',broker=CELERY_BROKER_URL,backend=CELERY_RESULT_BACKEND)

@celery.task
def satellite_tracker():
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=visual&FORMAT=tle"
    response = requests.get(url).text
    lines = response.strip().splitlines()
    satellites = []
    total_lines = len(lines)
    current_line = 0
    while current_line + 2 < total_lines:
        name = lines[current_line].strip()
        line1 = lines[current_line +1].strip()
        parts = line1.split()
        if len(parts)>1:
            norad_id = parts[1]
            satellites.append({"norad_id":norad_id,"name":name})
        current_line +=3

    with open("satellites.csv","w",newline="") as csvfile:
        writer = csv.DictWriter(csvfile,fieldnames=["norad_id","name"])
        writer.writeheader()
        writer.writerows(satellites)
