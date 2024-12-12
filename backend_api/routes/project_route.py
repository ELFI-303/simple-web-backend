from flask import jsonify,Blueprint

from utils.config import Config

from services.project_service import ProjectService

project_routes = Blueprint("project_routes", __name__)

@project_routes.route(Config.api_path()+"projects", methods=['GET'])
def api_projects():
    project_service = ProjectService()
    projects = project_service.get_projects()
    return jsonify(projects)

@project_routes.route(Config.api_path()+"projects/<id>", methods=['GET'])
def api_project(id: str):
    id = int(id)
    project_service = ProjectService()
    project = project_service.get_project(id)
    return jsonify(project)
