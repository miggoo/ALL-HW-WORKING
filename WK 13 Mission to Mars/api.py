import flask
from flask import request, jsonify
import os
import datetime as dt
# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pandas as pd
import numpy as np


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return (f"<h1>Welcome to the Hawaii search db<br/>"
           f"API routes:<br/>"
           f"/api/v1.0/precipitation<br/>"
           f"/api/v1.0/stations<br/>"
           f"/api/v1.0/"<start>"<br/>"
           f"/api/v1.0/"<start>"/"<end>"<br/>")


@app.route('/api/v1.0/precipitation', methods=['GET', 'POST'])
def api_all():
     

    return jsonify(books)


@app.route('/api/v1.0/stations', methods=['GET', 'POST'])
def api_all1():
    x = engine.execute('SELECT DISTINCT station FROM measurement').fetchall()
    


@app.route('/api/v1.0/<start>', methods=['GET', 'POST'])
            
def date(start):
    
 
    query1 = f"SELECT * FROM measurement WHERE date == {start}"
    
    date = engine.execute(query1).all()
    
    return jsonify(date)
   

app.run()
