from app.get_gps import get_gps

@get_gps.route('/test123')
def index()
    return {'Hello':'This is json data'}
