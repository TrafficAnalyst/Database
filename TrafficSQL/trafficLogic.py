import json 
import sqlite3 
import mysql.connector

class TrafficAnalystBackend: 
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3307,
            password="nafijoko",
            database="trafficgate"   
        )
        self.cursor = self.conn.cursor()

    def save_video (self,id_video,video,id_label,waktu_update): 
        try: 
            self.cursor.execute("INSERT INTO video (id_video,video,id_label,waktu_update) VALUES (?,?,?,)",(id_video,video,id_label,waktu_update))
            self.conn.commit()
            return True
        except Exception as e : 
            self.conn.rollback()
            print("Error:", str(e))
            return False    
    
    def save_kendaraan(self,id_kendaraan,waktu): 
        try: 
            self.cursor.execute("INSERT INTO kendaraan (id_kendaraan, waktu, sesi) VALUES (?,?,?)",(id_kendaraan,waktu))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_jumlahkendaraan(self,id_jumlahkendaraan,id_video,id_kendaraan,hari,waktu,sesi,jumlah_kendaraan,status): 
        try: 
            self.cursor.execute("INSERT INTO jumlahkendaraan (id_jumlahkendaraan,id_video,id_kendaraan,hari,waktu,jumlah_kendaraan,status) VALUES (?,?,?,?,?,?,?,?)",(id_jumlahkendaraan,id_video,id_kendaraan,hari,waktu,sesi,jumlah_kendaraan,status))
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False
        
    def close_connection(self):
        self.conn.close()
       