from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import sys
from moviepy.editor import VideoFileClip
import requests


sys.path.append('D:\WPy64-31130\scripts\Deteksi akhir')
from YoloDetek import detect_cars
sys.path.append('D:/WPy64-31130/scripts/Database/API-traffic/Data')
from video import Video
sys.path.append('D:/WPy64-31130/scripts/Database/API-traffic/Data')
from kendaraan import Kendaraan


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nafijoko@localhost:3307/trafficgate'  
db = SQLAlchemy(app)


UPLOAD_FOLDER = 'videoDate'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


DETECTION_FOLDER = 'hasildeteksi'
if not os.path.exists(DETECTION_FOLDER):
    os.makedirs(DETECTION_FOLDER)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DETECTION_FOLDER'] = DETECTION_FOLDER


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}  # Hanya izinkan beberapa ekstensi file video
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400
   
    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if not allowed_file(video_file.filename):
        return jsonify({'error': 'Invalid file type'}), 400


    # Ambil waktu unggah video
    upload_time = datetime.now()
    date_str = upload_time.strftime("%Y-%m-%d")
    current_time = upload_time.time()
    hari = upload_time.strftime("%A")
    waktu = upload_time.strftime("%H:%M:%S")


    if datetime(1900, 1, 1, 1, 0, 0).time() <= current_time < datetime(1900, 1, 1, 11, 0, 0).time():
        sesi = 'pagi'
    elif datetime(1900, 1, 1, 11, 0, 0).time() <= current_time < datetime(1900, 1, 1, 15, 0, 0).time():
        sesi = 'siang'
    else:
        sesi = 'sore'


    # Buat direktori berdasarkan tanggal dan sesi untuk video dan hasil deteksi
    date_folder = os.path.join(app.config['UPLOAD_FOLDER'], date_str)
    os.makedirs(date_folder, mode=0o755, exist_ok=True)
    output_folder = os.path.join(date_folder, sesi)
    os.makedirs(output_folder, mode=0o755, exist_ok=True)


    detection_folder = os.path.join(app.config['DETECTION_FOLDER'], date_str, sesi)
    os.makedirs(detection_folder, mode=0o755, exist_ok=True)


    filename = secure_filename(video_file.filename)
    video_path = os.path.join(output_folder, filename)


    try:
        video_file.save(video_path)


        id_video = os.path.splitext(filename)[0]


        video_data = Video(video=video_path, waktu=upload_time, sesi=sesi)
        db.session.add(video_data)
        db.session.commit()
       
        # Panggil fungsi deteksi kendaraan dengan video_path sebagai argumen
        detection_result = detect_cars(video_path)


        try:
            # Simpan video hasil deteksi dengan bounding box


            database_url = "https://wkf6l4sh-5000.asse.devtunnels.ms/insert_db"
            data_to_send = {
            "id_video": id_video,
            "jumlah_kendaraan": detection_result['jumlah_kendaraan'],
            "sesi": sesi
            }
            response = requests.post(database_url, json=data_to_send)


            return jsonify({'message': 'Video uploaded and detection results sent to database successfully'}), 200
        except Exception as e:
            return jsonify({'error': f'Failed to save detection video or send data to database: {str(e)}'}), 500


    except Exception as e:
        return jsonify({'error': f'Failed to upload video or send data to database: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
