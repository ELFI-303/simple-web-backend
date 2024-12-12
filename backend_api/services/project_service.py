from interface.project_interface import ProjectInterface
from models.project import Project
from utils.config import Config

class ProjectService:
    def __init__(self):
        self.interface = ProjectInterface()

    def get_project(self, id: int) -> dict:
        project = self.interface.get_project(id)
        project_object = Project(*project[0]).to_dict()
        return project_object
    
    def get_projects(self) -> list:
        projects = self.interface.get_projects()
        project_objects = [
            Project(*project).to_dict() for project in projects
        ]
        return self.add_links_to_projects(project_objects)

    def add_links_to_projects(self, projects: list) -> list:
        for project in projects:
            project["methods"] = {
                "self": f"{Config.api_path()}projects/{project['id']}",
            }
        return projects
