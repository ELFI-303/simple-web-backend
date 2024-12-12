from database.mysql_database import MySQLDatabase

class KahoutInterface:
    def __init__(self):
        self.db = MySQLDatabase().get_db()

    def get_kahouts(self) -> list:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM last_kahouts')
        kahouts = cursor.fetchall()
        return kahouts

    def get_kahout(self, id: int) -> str:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM last_kahouts WHERE kahout_id = %s', (id,))
        kahout = cursor.fetchall()
        return kahout
    
    def get_kahout_interviews(self, id: int) -> list:
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM kahout_interview WHERE kahout_id = %s', (id,))
        questions = cursor.fetchall()
        return questions
