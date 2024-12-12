class KahoutInterview:
    def __init__(self, id: int, question: str, reponse: str, taux: str) -> None:
        self.id = id
        self.question = question
        self.reponse = reponse
        self.taux = taux
        

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "reponse": self.reponse,
            "taux": self.taux
        }