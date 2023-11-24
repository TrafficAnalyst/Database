from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Kendaraan(db.Model):
    id_kendaraan = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jumlah_kendaraan = db.Column(db.Integer)
    status_kendaraan = db.Column(db.String(50))
    sesi = db.Column(db.String(10))
    id_video = db.Column(db.String(255))