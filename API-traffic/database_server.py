import mysql.connector

class ManagerDatabase:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3307,
            password="nafijoko",
            database="trafficgate"   
        )
        self.cursor = self.conn.cursor()
    
    def add_dataanalisis(self,id_video, id_kendaraan, hari, waktu, sesi, jumlah_kendaraan, status_arus):
        query = "INSERT INTO analisis(id_video, id_kendaraan, hari, waktu, sesi, jumlah_kendaraan, status_arus) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (id_video, id_kendaraan, hari, waktu, sesi, jumlah_kendaraan, status_arus)
        self.cursor.execute(query, values)
        self.conn.commit(),
    
    def add_datakendaraan(self,jumlah_kendaraan,status_kendaraan,sesi):
        query = "INSERT INTO kendaraan(jumlah_kendaraan,status_kendaraan,sesi) VALUES(%s, %s, %s)"
        values = (jumlah_kendaraan,status_kendaraan,sesi)
        self.cursor.execute(query, values)
        self.conn.commit()
    
    def add_video(self,video,waktu):
        placeholders = ', '.join(['%s'] * len(data))
        query = "INSERT INTO video(video,waktu) VALUES(%s, %s)"
        values = (video,waktu)
        self.cursor.execute(query, values)
        self.conn.commit()

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            port=3307,
            password="nafijoko",
            database="trafficgate"   
        )
        self.cursor = self.conn.cursor()
    
    def get_kendaraan_by_id(self,id_kendaraan):
        query = "SELECT * FROM kendaraan WHERE id_kendaraan= %s"
        values = (id_kendaraan,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()
    
    def get_video_by_id(self,id_video):
        query = "SELECT * FROM video WHERE id_video= %s"
        values = (id_video,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def get_analisis_by_id(self,id_analisis):
        query = "SELECT * FROM analisis WHERE id_analisis= %s"
        values = (id_analisis,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def get_analisis(self):
        try:
            query = "SELECT * FROM analisis"
            self.cursor.execute(query)

            analisis_data = self.cursor.fetchall()
            
            # Ubah data menjadi list of dictionaries
            data_list = []
            for row in analisis_data:
                data_dict = {
                    "id_analisis": row[0],
                    "id_video": row[1],
                    "id_kendaraan": row[2],
                    "hari": row[3],
                    "waktu": row[4],
                    "sesi": row[5],
                    "jumlah_kendaraan": row[6],
                    "status_kendaraan": row[7]
                }
                data_list.append(data_dict)

            return data_list
        except Exception as e:
            print("Error:", e)
            return []
    
    def get_kendaraan(self):
        try:
            query = "SELECT * FROM kendaraan"
            self.cursor.execute(query)

            kendaraan_data = self.cursor.fetchall()
            return kendaraan_data
        except Exception as e:
            print("Error:", e)
            return []

    def get_video(self):
        try:
            query = "SELECT * FROM video"
            self.cursor.execute(query)

            video_data = self.cursor.fetchall()
            return video_data
        except Exception as e:
            print("Error:", e)
            return []
        
    def close_connection(self):
        self.connection.close()
        