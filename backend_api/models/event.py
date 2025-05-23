class Event:
    def __init__(self, id: int, title: str, description: str, date: str, place: str, url_img: str, link: str) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.place = place
        self.url_img = url_img
        self.link = link

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "place": self.place,
            "url_img": self.url_img,
            "link": self.link
        }