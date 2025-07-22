from app.get_gps import get_gps
from flask import request
import requests
import math
@get_gps.route('/my_gps',methods=['POST'])
def my_gps():
    """
    यहाँ API को endpoint function define गरिएको छ,
    जसले ISS र user को बीचको distance return गर्छ।
    """
    iss_location = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_location_values = iss_location['iss_position']
    lon1 = iss_location_values['longitude']
    lat1 = iss_location_values['latitude']
    if request.method== 'POST':
        my_location_values= request.get_json()
        data = my_location_values['location'].split(',')
        lon2,lat2=data[0],data[1]

        distance=haversine(float(lat1),float(lon1),float(lat2),float(lon2))
        return {'Distance':distance}


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
