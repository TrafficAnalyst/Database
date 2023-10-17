
from trafficLogic import TrafficAnalystBackend

if __name__ == "__main__" : 
    backend = TrafficAnalystBackend()
    backend.create_tables()
    backend.close_connection()