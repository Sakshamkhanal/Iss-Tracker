from flask import Flask,request
import requests
app = Flask(__name__)

@app.route('/iss_gps',methods=['GET'])
def get_gps():
    data = requests.get("http://api.open-notify.org/iss-now.json")
    return data.json()

@app.route('/my_gps',methods=['POST'])
def my_gps():
    if request.method== 'POST':
        temp_location = request.get_json()
        print(temp_location)
