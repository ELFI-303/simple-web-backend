from flask import jsonify,Blueprint

from utils.config import Config

from services.kahout_service import KahoutService

kahout_routes = Blueprint("kahout_routes", __name__)

@kahout_routes.route(Config.api_path()+"kahouts", methods=['GET'])
def api_kahouts():
    kahout_service = KahoutService()
    kahouts = kahout_service.get_kahouts()
    return jsonify(kahouts)

@kahout_routes.route(Config.api_path()+"kahouts/<id>", methods=['GET'])
def api_kahout(id: str):
    id = int(id)
    kahout_service = KahoutService()
    kahout = kahout_service.get_kahout(id)
    return jsonify(kahout)

@kahout_routes.route(Config.api_path()+"kahouts/<id>/interview", methods=['GET'])
def api_kahout_interview(id: str):
    id = int(id)
    kahout_service = KahoutService()
    interviews = kahout_service.get_interviews(id)
    return jsonify(interviews)

