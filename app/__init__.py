from config import Config
from flask import Flask

from .extensions import celery, db, migrate


def create_app(config_class=Config):
    '''
     यो file मा Flask app लाई initalzie  गरिएको छ।
    साथै, database र migrate पनि यहीं initalize  गरिएको छ।
    सबै sub-module हरूका blueprint हरू register गरिएको छ
    र Celery पनि यहीं initalize  गरिएको छ।
    '''
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.get_gps import get_gps as main_get_gps

    app.register_blueprint(main_get_gps)

    init_celery(app)

    return app


def init_celery(app=None):
    '''
    यो function initialize ले Flask एप्लिकेसनसँग Celery integrate  गर्छ।

    यदि `app` दिइएको छैन भने नयाँ application  बनाइन्छ `create_app()` बाट।
    त्यसपछि Flask एपको कन्फिगरेसन Celery मा अपडेट गरिन्छ।

    ContextTask नामको custom Task क्लास बनाइएको छ जसले Celery टास्कहरूलाई
    Flask को application context भित्र run गराउँछ।

    यसले Celery task हरूलाई Flask app को config, database session,
    र अन्य context elements प्रयोग गर्न अनुमति दिन्छ।

    अन्त्यमा Celery को default Task क्लासलाई ContextTask बाट override गरिएको छ।
    '''
    app = app or create_app()
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
