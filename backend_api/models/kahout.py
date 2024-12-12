class Kahout:
    def __init__(self, id: int, title: str, date: str, img_url: str) -> None:
        self.id = id
        self.title = title
        self.date = date
        self.img_url = img_url

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date,
            "img_url": self.img_url
        }