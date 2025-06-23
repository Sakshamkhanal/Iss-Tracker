from flask import Flask,request
import requests
import math
app = Flask(__name__)

@app.route('/iss_gps',methods=['GET'])
def get_gps():
    data = requests.get("http://api.open-notify.org/iss-now.json")
    return data.json()

@app.route('/my_gps',methods=['POST'])
def my_gps():
    iss_location = requests.get("http://api.open-notify.org/iss-now.json").json()
    iss_location_values = iss_location['iss_position']
    lon1 = iss_location_values['longitude']
    lat1 = iss_location_values['laltitude']
    import pdb;pdb.set_trace();
    if request.method== 'POST':
        my_location_values= request.get_json().split(',')
        lon2,lat2=data[0],data[1]

        haversine(lat1,lon1,lat2,lon2)

#Using haversine formula to calculate the distance
def haversine(lat1,lon1,lat2,lon2):
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
