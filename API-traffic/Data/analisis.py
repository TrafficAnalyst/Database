from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Analisis(db.Model):
    id_analisis = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_video = db.Column(db.String(255))
    id_kendaraan = db.Column(db.Integer)
    hari = db.Column(db.String(20))
    waktu = db.Column(db.DateTime)
    jumlah_kendaraan = db.Column(db.Integer)
    status_arus = db.Column(db.String(20))
    sesi = db.Column(db.String(10))