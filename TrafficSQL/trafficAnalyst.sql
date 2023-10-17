CREATE DATABASE IF NOT EXISTS trafficgate;
USE trafficgate;

CREATE TABLE IF NOT EXISTS video (
  id_video INT AUTO_INCREMENT PRIMARY KEY,
  video VARCHAR (255),
  waktu TIMESTAMP
);

CREATE TABLE IF NOT EXISTS kendaraan(
  id_kendaraan INT AUTO_INCREMENT PRIMARY KEY,
  jumlah_kendaraan INT,
  status_kendaraan VARCHAR(255),
  sesi VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS analisis(
  id_analisis INT AUTO_INCREMENT PRIMARY KEY,
  id_video INT, 
  id_kendaraan INT, 
  hari VARCHAR (255) ,
  waktu TIMESTAMP,
  sesi VARCHAR (50),
  jumlah_kendaraan INT,
  status_arus VARCHAR (50),
  FOREIGN KEY (id_video) REFERENCES video(id_video),
  FOREIGN KEY (id_kendaraan) REFERENCES kendaraan(id_kendaraan)
);
