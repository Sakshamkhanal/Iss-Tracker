from app.get_gps import get_gps
from flask import request,Flask
import requests
import math
from app.tasks  import get_satellites
from skyfield.api import EarthSatellite
from skyfield.api import load,wgs84
from skyfield.positionlib import Geocentric
import datetime as dt
from pytz import timezone
@get_gps.route('/my_gps',methods=['POST'])
def my_gps():
    """
    यहाँ API को endpoint function define गरिएको छ,
    जसले ISS र user को बीचको distance return गर्छ।
    """
    starlink1="""
    STARLINK-31857
    1 59843U 24097J   24152.50001157 -.00832730  00000+0 -40214-2 0  9991
    2 59843  43.0045   5.2275 0001736 273.1057  88.8863 15.83654368  2541
    """
    #get_satellites.delay()
    iss_location = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_location_values = iss_location['iss_position']
    lon1 = iss_location_values['longitude']
    lat1 = iss_location_values['latitude']
    if request.method== 'POST':
        my_location_values= request.get_json()
        data = my_location_values['location'].split(',')
        lon2,lat2=data[0],data[1]

        distance=haversine(float(lat1),float(lon1),float(lat2),float(lon2))

        satellite_values = trajectory(starlink1)
        return satellite_values


#Using haversine formula to calculate the distance
def haversine(lat1,lon1,lat2,lon2):
    """
    यो haversine formula को implementation हो,
    जसले दुई GPS coordinates बीचको दूरी (distance) गणना गर्छ।
    """

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    dlat = lat2-lat1
    dlon = lon2-lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    R = 6371.0
    distance = R*c
    return distance

def trajectory(tle_text):
    """
    यो function मा चैं text को processing गरिन्छ ।
    tle चैं database बाट data query गरेर निकाल्ने हो,
    अनि त्यसपछि त्यसलाई process गरिन्छ ।
    """
    lines = tle_text.strip().splitlines()
    sat = EarthSatellite(lines[1],lines[2],lines[0])


    zone = timezone('Asia/Kathmandu')
    now = zone.localize(dt.datetime.now())
    ts = load.timescale()
    t  = ts.from_datetime(now)
    geo = sat.at(t)

    lat,lon = wgs84.latlon_of(geo)
    height = wgs84.height_of(geo)
    return {'latitue':lat}
