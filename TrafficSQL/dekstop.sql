CREATE DATABASE IF NOT EXISTS dekstop;
USE dekstop;

CREATE TABLE IF NOT EXISTS petugas(
  id_petugas INT AUTO_INCREMENT PRIMARY KEY,
  nama VARCHAR (50),
  pws INT (11)
);

CREATE TABLE IF NOT EXISTS jumlah_ken(
  id_jumlah INT AUTO_INCREMENT PRIMARY KEY,
  id_video INT (11), 
  id_kendaraan INT (11), 
  hari VARCHAR (255) ,
  waktu TIMESTAMP,
  sesi VARCHAR (50),
  jumlah_kendaraan INT (11),
  status_arus VARCHAR (50),
);
