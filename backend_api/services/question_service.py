from interface.question_interface import QuestionInterface
from interface.mail_interface import MailInterface
from models.question import Question

class QuestionService:
    def __init__(self):
        self.question = QuestionInterface()
        self.mail = MailInterface()

    def send_question(self, question: Question) -> str:
        self.question.send_question(question)
        self.mail.construct(question)

