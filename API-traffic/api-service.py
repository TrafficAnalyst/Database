from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import os
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from database_server import ManagerDatabase

app = Flask(__name__)
db_manager = ManagerDatabase()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:nafijoko@localhost:3307/trafficgate'
db = SQLAlchemy(app)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}  
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

UPLOAD_FOLDER = 'D:\WPy64-31130\scripts\Database\API-traffic/videoDate'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file uploaded'}), 400

    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if not allowed_file(video_file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    try:
        # Kirim video langsung ke port 4000 untuk disimpan di direktori
        upload_url = "https://wkf6l4sh-4000.asse.devtunnels.ms/upload_video"
        files = {'video': (video_file.filename, video_file)}
        response = requests.post(upload_url, files=files)

        return jsonify({'message': 'Video uploaded successfully'}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to upload video: {str(e)}'}), 500

if __name__ == '__main__':
    app.config['JSONIFY_TIMEOUT'] = 120  # Menetapkan timeout untuk fungsi jsonify
    app.run(host='0.0.0.0', port=3000, debug=True, threaded=True, processes=1)

