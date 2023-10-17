from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Fungsi untuk mengambil data dari API database
def get_data_from_database():
    # Gantilah URL dengan URL API database Anda
    database_url = ""
    response = requests.get(database_url)
    data = response.json()
    return data

# Fungsi untuk melakukan prediksi menggunakan API machine learning
def predict_using_ml(data):
    # Gantilah URL dengan URL API machine learning Anda
    ml_url = ""
    response = requests.post(ml_url, json=data)
    prediction = response.json()
    return prediction

@app.route('/get-deteksi', methods=['POST'])
def get_prediction():
    try:
        # Mengambil data dari API database
        database_data = get_data_from_database()

        # Melakukan prediksi menggunakan API machine learning
        prediction = predict_using_ml(database_data)

        return jsonify({"prediction": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)