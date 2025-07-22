from flask import Blueprint
# यहाँ Blueprint हरूलाई integrate गरिएको छ।

get_gps = Blueprint('get_gps',__name__)

from app.get_gps import routes
