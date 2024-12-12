from flask import jsonify,Blueprint

from utils.config import Config
from services.event_service import EventService


event_routes = Blueprint("event_routes", __name__)

@event_routes.route(Config.api_path()+"events", methods=['GET'])
def api_events():
    event_service = EventService()
    events = event_service.get_events()
    return jsonify(events)

@event_routes.route(Config.api_path()+"events/<id>", methods=['GET'])
def api_event(id: str):
    id = int(id)
    event_service = EventService()
    event = event_service.get_event(id)
    return jsonify(event)