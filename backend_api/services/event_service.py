# services/event_service.py
from database.mysql_database import MySQLDatabase
from models.event import Event
from config.config import Config

class EventService:
    def __init__(self):
        db_config = Config.get_database_config()
        self.db = MySQLDatabase(db_config)

    def get_event(self,event_id):
        event = self.db.get_event(event_id)
        event_object = Event(*event[0]).to_dict()
        return event_object
    
    def get_events(self):
        events = self.db.get_events()
        event_objects = [
            Event(*event).to_dict() for event in events
        ]
        return self.add_links_to_events(event_objects)

    def add_links_to_events(self, events):
        for event in events:
            event["methods"] = {
                "self": f"/api/v1/events/{event['event_id']}",
            }
        return events
