from flask import Flask,jsonify
from werkzeug.exceptions import HTTPException

from utils.config import Config
from routes.event_route import event_routes
from routes.kahout_route import kahout_routes
from routes.project_route import project_routes
from routes.message_route import message_routes

application = Flask(__name__)


application.register_blueprint(event_routes)
application.register_blueprint(kahout_routes)
application.register_blueprint(project_routes)
application.register_blueprint(message_routes)

@application.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    }).get_data(as_text=True)
    response.content_type = "application/json"
    return response

@application.errorhandler(Exception)
def handle_generic_exception(e):
    application.logger.error(f"Unhandled exception: {e}")
    return jsonify({"error": "An internal error occurred. Please try again later."}), 500

if __name__ == "__main__":
    application.run(host=Config.get_run_config()[0], port=Config.get_run_config()[1], debug=True)
