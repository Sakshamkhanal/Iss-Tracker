from config import Config
from flask import Flask

from .extensions import celery, db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.get_gps import get_gps as main_get_gps

    app.register_blueprint(main_get_gps)

    init_celery(app)

    return app


def init_celery(app=None):
    app = app or create_app()
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
