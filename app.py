from flask import Flask
from Iss_Tracker.database import db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route("/get_gps")
def get_gps():
    return{"Hello":"World"}
