class Event:
    def __init__(self, event_id, title, description, date, place, img_url, link):
        self.event_id = event_id
        self.title = title
        self.description = description
        self.date = date
        self.place = place
        self.img_url = img_url
        self.link = link

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "place": self.place,
            "img_url": self.img_url,
            "link": self.link
        }