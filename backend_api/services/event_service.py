from interface.event_interface import EventInterface
from models.event import Event
from utils.config import Config

class EventService:
    def __init__(self):
        self.interface = EventInterface()

    def get_event(self, id: int) -> dict:
        event = self.interface.get_event(id)
        event_object = Event(*event[0]).to_dict()
        return event_object
    
    def get_events(self) -> list:
        events = self.interface.get_events()
        event_objects = [
            Event(*event).to_dict() for event in events
        ]
        return self.add_links_to_events(event_objects)

    def add_links_to_events(self, events: list) -> list:
        for event in events:
            event["methods"] = {
                "self": f"{Config.api_path()}events/{event['id']}",
            }
        return events
