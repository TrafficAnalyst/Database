from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Fungsi untuk melakukan prediksi menggunakan API machine learning
def predict_using_ml(data):
    # Gantilah URL dengan URL API machine learning Anda
    ml_url = "https://csbnpmnk-5000.asse.devtunnels.ms/"
    response = requests.post(ml_url, json=data)
    prediction = response.json()
    return prediction

# Fungsi untuk mengirim data ke API database
def send_data_to_database(data):
    # Gantilah URL dengan URL API database Anda yang menerima data melalui POST
    database_url = "https://csbnpmnk-8080.asse.devtunnels.ms/"
    response = requests.post(database_url, json=data)
    return response.json()

@app.route('/get-prediction', methods=['POST'])
def get_prediction():
    try:
        # Mengambil data dari API database
        
        data_to_send = {"key1": "value1", "key2": "value2"}  # Gantilah dengan data yang sesuai
        send_data_to_database(data_to_send)

        # Melakukan prediksi menggunakan API machine learning
        prediction = predict_using_ml(data_to_send)

        return jsonify({"prediction": prediction}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)