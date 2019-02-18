
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



#DB SETUP
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

dict_1 = session.query(Measurement.prcp, Measurement.date).order_by(Measurement.date.desc())\
    .filter(Measurement.date > '2016-08-23').all()
# API SECTION
app = Flask(__name__)


@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
            f"Welcome to my 'Home' page! </br>" 
            f"Available routes:</br>"
            f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f"/api/v1.0/<start>"
            f"/api/v1.0/<start>/<end>"
        )


@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Precipitation data")
    all_precip_data = []
    for d in dict_1:
        precip_dict = {}
        precip_dict['date'] = Measurement.date
        precip_dict['prcp'] = Measurement.prcp
        all_precip_data.append(precip_dict)
    return jsonify(all_precip_data)

#@app.route("/api/v1.0/stations")
#def stations():


#@app.route("/api/v1.0/tobs")
#def tobs():

#@app.route("/api/v1.0/<start>")
#def 

#@app.route("/api/v1.0/<start>/<end>")


if __name__ == "__main__":
    app.run(debug=True)

