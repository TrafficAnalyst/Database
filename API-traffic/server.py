from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

import database_server as db

app = Flask(__name__)

video_directory = "video"

db_manager= db.ManagerDatabase()

@app.route("/", methods=['GET'])
def hello():
    return jsonify(status="running")

#memasukkan data Video
@app.route("/insert_video", methods=['POST'])
def insert_video():
    try:
        # Menerima file gambar dari permintaan POST
        if 'video' in request.files:
            image = request.files['video']
            
            # Pastikan direktori "gambar" ada
            if not os.path.exists(video_directory):
                os.makedirs(image_directory)
            
            # Simpan file gambar ke direktori "gambar"
            video = os.path.join(video_directory, video.filename)
            video.save(video)
            
            # Simpan path gambar ke database
            db_manager.insert_video(video)
            
            return jsonify({"message": "Video inserted successfully"})
        else:
            return jsonify({"error": "No video file found in the request"})
    except Exception as e:
        return jsonify({"error": str(e)})

#MEMASUKKAN DATA KENDARAAN 

@app.route("/insert_kendaraan", methods=['POST'])
def insert_kendaraan():
    try:
        data = request.get_json()
        db_manager.insert_kendaraan(data["jumlah_kendaraan"], data["status_kendaraan"],data["sesi"])
        return jsonify({"message": "kendaraan inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

#MEMASUKKAN DATA ANALISIS 
@app.route("/insert_analisis", methods=['POST'])
def insert_analisis():
    try:
        data = request.get_json()
        db_manager.insert_analisis(data["id_video"], data["id_kendaraan"],data["hari"], data["waktu"],data["sesi"],data["jumlah_kendaraan"], data["status_kendaraan"])
        return jsonify({"message": "analisis inserted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})

#MENAMPILKAN TABEL ANALISIS  
@app.route('/dataanalisis', methods=['GET'])
def data_analisis():
    analisis_data = db_manager.get_analisis()
    if not analisis_data:
        return jsonify(message="Data not found"), 404

    return jsonify(analisis_data=analisis_data)

#MENAMPILKAN DATA KENDARAAN 
@app.route('/datakendaraan', methods=['GET'])
def data_kendaraan():
    kendaraan_data = db_manager.get_kendaraan()
    if not kendaraan_data:
        return jsonify(message="Data not found"), 404

    return jsonify(kendaraan_data=kendaraan_data)

#MENAMPILKAN DATA VIDEO 
@app.route('/datavideo', methods=['GET'])
def data_video():
    video_data = db_manager.get_video()
    if not video_data:
        return jsonify(message="Data not found"), 404

    return jsonify(video_data=video_data)

#MENAMPILKAN DATA SATU DATABASE 
@app.route('/datatraffic', methods=['GET'])
def data_traffic():
    analisis_data = db_manager.get_analisis()
    if not analisis_data:
        return jsonify(message="Data analisis not found"), 404

    kendaraan_data = db_manager.get_kendaraan()
    if not kendaraan_data:
        return jsonify(message="Data kendaraan not found"), 404

    video_data = db_manager.get_video()
    if not video_data:
        return jsonify(message="Data video not found"), 404

    return jsonify(analisis_data=analisis_data, kendaraan_data=kendaraan_data, video_data=video_data)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    