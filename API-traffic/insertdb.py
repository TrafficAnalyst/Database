import requests

server_url = "http://127.0.0.1:5000"

kendaraan_data = {
    "id_kendaraan": 3,
    "jumlah_kendaraan": 10,
    "status_kendaraan": "sepi",
    "sesi": "pagi"
}
video_data = {
    "id_video": 3,
    "nama_video": "path/to/video4.mp4",
    "waktu_update": "2023-10-11"
}
analisis_data = {
    "id_analisis": 4,
    "id_video": 2,
    "id_kendaraan": 1,
    "hari": "rabu",
    "waktu": "2023-10-11",
    "sesi": "sepi",
    "jumlah_kendaraan": 10,
    "status_kendaraan": "sepi"
}

try:
    # Mengirim data untuk tabel "jumlahtransportasi"
    response = requests.post(f"{server_url}/insert_kendaraan", json=kendaraan_data)
    if response.status_code == 200:
        print("Data jumlah kendaraan berhasil disimpan ke database.")
    else:
        print(f"Gagal menyimpan data jumlah kendaraan. Kode status: {response.status_code}")

    # Mengirim data untuk tabel "images"
    response = requests.post(f"{server_url}/insert_video", json=video_data)
    if response.status_code == 200:
        print("Data video berhasil disimpan ke database.")
    else:
        print(f"Gagal menyimpan data video. Kode status: {response.status_code}")

    # Mengirim data untuk tabel "jenis_transportasi"
    response = requests.post(f"{server_url}/insert_analisis", json=analisis_data)
    if response.status_code == 200:
        print("Data analisis berhasil disimpan ke database.")
    else:
        print(f"Gagal menyimpan data analisis. Kode status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Gagal melakukan permintaan ke API: {str(e)}")
