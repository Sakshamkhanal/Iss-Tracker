from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from flask_migrate import Migrate

db = SQLAlchemy()
celery = Celery()
migrate = Migrate()
