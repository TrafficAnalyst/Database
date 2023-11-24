from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import database_server as db
import sys 
sys.path.append('D:/WPy64-31130/scripts/Database/API-traffic/Data')
from video import Video
sys.path.append('D:/WPy64-31130/scripts/Database/API-traffic/Data')
from kendaraan import Kendaraan
sys.path.append('D:/WPy64-31130/scripts/Database/API-traffic/Data')
from analisis import Analisis

app = Flask(__name__)

db_manager= db.ManagerDatabase()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nafijoko@localhost:3307/trafficgate' 
db = SQLAlchemy(app)

video_directory = "video"
deteksi_akhir_folder = "D:\WPy64-31130\scripts\Deteksi akhir"

def get_status_kendaraan(jumlah_kendaraan):
    if jumlah_kendaraan <= 30:
        return "sepi"
    elif jumlah_kendaraan <= 60:
        return "renggang"
    else:
        return "padat"

@app.route("/", methods=['GET'])
def hello():
    return jsonify(status="running")

#memasukkan data Video
@app.route('/save_video', methods=['POST'])
def save_video():
    try:
        data = request.get_json()

        video_path = data["video"]
        upload_time = datetime.now()
        sesi = data["sesi"]

        video_data = Video(video=video_path, waktu=upload_time, sesi=sesi)
        db.session.add(video_data)
        db.session.commit()

        return jsonify({'message': 'Video uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to upload database: {str(e)}'}), 500

#MEMASUKKAN DATA KENDARAAN 
@app.route('/insert_db', methods=['POST'])
def insert_kendaraan():
    try:
        data = request.get_json()
        
        jumlah_kendaraan = data["jumlah_kendaraan"]
        sesi = data["sesi"]
        id_video = data["id_video"]
        
        status_kendaraan = get_status_kendaraan(jumlah_kendaraan)

        kendaraan_data = Kendaraan(jumlah_kendaraan=jumlah_kendaraan, status_kendaraan=status_kendaraan, sesi=sesi, id_video=id_video)

        db.session.add(kendaraan_data)
        db.session.commit()

        id_kendaraan = kendaraan_data.id_kendaraan

        print(id_kendaraan)

        waktu = datetime.now()
        hari = waktu.strftime("%A")

        print(hari)

        analisis_data = Analisis(hari=hari, waktu=waktu, sesi=sesi, jumlah_kendaraan=jumlah_kendaraan, status_arus=status_kendaraan, id_video=id_video, id_kendaraan=id_kendaraan)

        db.session.add(analisis_data)
        db.session.commit()

        return jsonify({'message': 'Kendaraan data inserted successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to insert kendaraan data: {str(e)}'}), 500


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
    