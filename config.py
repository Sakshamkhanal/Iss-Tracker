import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql://user_saksham:5456@localhost/iss_tracking"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    celery_broker_url =  'redis://localhost:6379/0'
    celery_result_backend = 'redis://localhost:6379/0'
