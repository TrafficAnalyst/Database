#FILE UNTUK MEMASUKAN HASIL VIDEO KE TABEL VIDEO 

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Tentukan direktori penyimpanan file video
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nafijoko@localhost:3307/trafficgate' # Sesuaikan dengan konfigurasi database Anda
db = SQLAlchemy(app)

class Video(db.Model):
    id_video = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video = db.Column(db.String(255))
    waktu = db.Column(db.DateTime)

# Fungsi bantu untuk memeriksa ekstensi file yang diunggah
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}  # Hanya izinkan beberapa ekstensi file video
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_video', methods=['POST'])
def upload_video():
    # Periksa apakah ada file yang diunggah
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400
    
    video_file = request.files['video']

    # Periksa apakah file yang diunggah memiliki nama file dan ekstensi yang benar
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if not allowed_file(video_file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    # Aman nama file untuk menghindari serangan injeksi
    filename = secure_filename(video_file.filename)

    # Simpan file di direktori upload
    video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Simpan informasi video ke database
    waktu = datetime.now()
    new_video = Video(video=filename, waktu=waktu)

    # Buat konteks aplikasi sebelum menjalankan db.create_all()
    with app.app_context():
        db.session.add(new_video)
        db.create_all()
        db.session.commit()

    return jsonify({'message': 'Video uploaded successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
