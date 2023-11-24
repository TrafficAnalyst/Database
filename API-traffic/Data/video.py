from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Video(db.Model):
    id_video= db.Column(db.Integer, primary_key=True, autoincrement=True)
    video = db.Column(db.String(255))
    waktu = db.Column(db.DateTime)
    sesi = db.Column(db.String(10))