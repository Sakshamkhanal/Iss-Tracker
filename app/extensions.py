from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_migrate import Migrate

db = SQLAlchemy()
celery = Celery()
migrate = Migrate()

# यहाँ SQLAlchemy, Celery र Flask-Migrate हरू इनिशियलाइज गरिएको छ, 
# त्यसैले यो अरू ठाउँमा इम्पोर्ट हुन्छ।

