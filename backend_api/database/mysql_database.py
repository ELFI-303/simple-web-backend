import mysql.connector
from database.database_interface import Database

class MySQLDatabase(Database):
    def __init__(self, config):
        self.config = config

    def get_events(self):
        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM events_incomming')
        events = cursor.fetchall()
        return events
    
    def get_event(self,event_id):
        db = mysql.connector.connect(**self.config)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM events_incomming WHERE event_id = %s', (event_id,))
        event = cursor.fetchall()
        return event