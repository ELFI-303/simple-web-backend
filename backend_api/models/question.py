from datetime import datetime
from dateutil.parser import parse

class Question:
    def __init__(self, date: datetime, nom: str, email: str, message: str) -> None:
        self.date = parse(date)
        self.nom = nom
        self.email = email
        self.message = message

    def to_dict(self):
        return {
            "date": self.date,
            "nom": self.nom,
            "email": self.email,
            "message": self.message,
        }