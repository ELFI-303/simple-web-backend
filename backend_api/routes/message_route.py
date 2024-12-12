from flask import request,Blueprint,current_app
import json

from utils.config import Config
from models.question import Question
from services.question_service import QuestionService

message_routes = Blueprint("message_routes", __name__)

@message_routes.route(Config.api_path()+"send", methods=['POST'])
def api_send_question():
    response = request.get_json(force=True)
    question = Question(response["date"],response["nom"],response["email"],response["message"])
    question_service = QuestionService()
    question_service.send_question(question)
    return "Email succesfully sended!",200
