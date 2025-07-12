from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config.from_mapping(
        CELERY=dict(
            broker_url='redis://localhost',
            result_backend="redds://localhost",
            task_ignore_result=True.
            ),
            )


    from app.get_gps import get_gps as main_get_gps
    app.register_blueprint(main_get_gps)

    #@app.route('/test/')
    #def test_page():
    #   return '<h1>Testing the Flask APplication Factory Pattern</h1>'

    celery_app = celery_init_app(app)
    return app
