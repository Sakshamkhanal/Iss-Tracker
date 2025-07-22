from app.extensions import db

class SatelliteTLE(db.Model):
    """
    यहाँ Celestrak बाट JSON response अनुसार models बनाइएको छ।
    यो Celery task ले data हरू load गर्दा सो डेटा यो table मा insert वा update गर्छ।
    """

    __tablename__ = 'satellite_tles'

    id = db.Column(db.Integer,primary_key=True)
    object_name = db.Column(db.String(128))
    object_id = db.Column(db.String(32))
    epoch = db.Column(db.String(32))
    mean_motion = db.Column(db.Float)
    eccenetricity = db.Column(db.Float)
    inclination = db.Column(db.Float)
    ra_of_asc_node = db.Column(db.Float)
    mean_anomaly = db.Column(db.Float)
    classification_type = db.Column(db.String(8))
    norad_cat_id = db.Column(db.Integer,index=True)
    element_set_no = db.Column(db.Integer)
    rev_at_epoch = db.Column(db.Integer)
    bstar = db.Column(db.Float)
    mean_motion_dot = db.Column(db.Float)
    mean_motion_ddot = db.Column(db.Float)
