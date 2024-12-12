from database.mysql_database import MySQLDatabase
from models.question import Question

class QuestionInterface:
    def __init__(self):
        self.db = MySQLDatabase().get_db()

    def send_question(self, question: Question) -> str:
        cursor = self.db.cursor()
        cursor.execute("INSERT INTO question_received (question_received_id, question_date, nom, email, message_envoye) VALUES (NULL, %s, %s, %s, %s)", 
                       (question.date.strftime('%Y-%m-%d %H:%M:%S'), question.nom, question.email, question.message))
        self.db.commit()