from interface.kahout_interface import KahoutInterface
from models.kahout import Kahout
from models.kahout_interview import KahoutInterview
from utils.config import Config

class KahoutService:
    def __init__(self):
        self.interface = KahoutInterface()

    def get_kahout(self, id: int) -> dict:
        kahout = self.interface.get_kahout(id)
        kahout_object = Kahout(*kahout[0]).to_dict()
        return kahout_object

    def get_kahouts(self) -> list:
        kahouts = self.interface.get_kahouts()
        kahout_objects = [
            Kahout(*kahout).to_dict() for kahout in kahouts
        ]
        return self.add_links_to_kahouts(kahout_objects)

    def add_links_to_kahouts(self, kahouts: list) -> list:
        for kahout in kahouts:
            kahout["methods"] = {
                "self": f"{Config.api_path()}kahouts/{kahout['id']}",
            }
        return kahouts
    
    def get_interviews(self, id: int) -> list:
        interviews = self.interface.get_kahout_interviews(id)
        interview_objects = [
            KahoutInterview(*interview).to_dict() for interview in interviews
        ]
        return interview_objects
