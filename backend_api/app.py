from flask import Flask, jsonify
from config.config import Config
from services.event_service import EventService

app = Flask(__name__)

@app.route("/api/v1/events", methods=['GET'])
def api_events():
    event_service = EventService()
    events = event_service.get_events()
    return jsonify(events)

@app.route("/api/v1/events/<event_id>", methods=['GET'])
def api_event(event_id):
    event_service = EventService()
    event = event_service.get_event(event_id)
    return jsonify(event)


if __name__ == "__main__":
    host, port = Config.get_run_config()
    app.run(host=host, port=port, debug=True)
