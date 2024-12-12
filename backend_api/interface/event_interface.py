from database.mysql_database import MySQLDatabase

class EventInterface:
    def __init__(self):
        self.db = MySQLDatabase().get_db()

    def get_events(self) -> str:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM incomming_events')
        events = cursor.fetchall()
        return events

    def get_event(self, id: int) -> str:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM incomming_events WHERE event_id = %s', (id,))
        event = cursor.fetchall()
        return event