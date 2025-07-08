from flask import Blueprint

get_gps = Blueprint('get_gps',__name__)

from app.get_gps import routes
