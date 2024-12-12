import smtplib
import ssl

from email.message import EmailMessage
from models.question import Question
from utils.config import api_mail
from utils.mail import get_body,get_html_body

from flask import current_app

class MailInterface:
    def __init__(self):
        self.info = api_mail()

    def construct(self, question: Question) -> EmailMessage:
        em = EmailMessage()
        em['From'] = self.info["sendMail"]
        em['To'] = self.info["receiver"]
        em['Subject'] = f"Nouveau message de {question.nom}"
        em.set_content(get_body())
        em.add_alternative(get_html_body(), subtype='html')
        return em

    def send_mail(self, em: EmailMessage) -> None:
        try:
            context = ssl.create_default_context()
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(em['From'], self.info["sendPass"])
                smtp.sendmail(em['From'], self.info["receiver"], em.as_string())
        
        except smtplib.SMTPException as e:
            current_app.logger.error(f"An SMTP error occurred: {e}")