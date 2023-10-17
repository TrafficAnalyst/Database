from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import os
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'trafficgate'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route("/", methods=['GET'])
def hello():
    return jsonify(status= "running")