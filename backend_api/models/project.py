class Project:
    def __init__(self, id: int, title: str, description: str, date: str, place: str, img_url: str, link: str, equipe: str) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.place = place
        self.img_url = img_url
        self.link = link
        self.equipe = equipe.split(",")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "place": self.place,
            "img_url": self.img_url,
            "link": self.link,
            "equipe": self.equipe
        }