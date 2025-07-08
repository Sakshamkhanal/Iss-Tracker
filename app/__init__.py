from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.get_gps import get_gps as main_get_gps
    app.register_blueprint(main_get_gps)

    #@app.route('/test/')
    #def test_page():
    #   return '<h1>Testing the Flask APplication Factory Pattern</h1>'

    return app
