from fastapi import Request, Depends
from requests import Session

from src.configuration import Database
from src.service.AIAgentService import AIAgentService
from src.service.UserService import UserService


def get_ai_agent_service(request: Request,
                         db: Session = Depends(Database.get_db)) -> AIAgentService:
    return AIAgentService(request.app.state.llm_model,db)


def get_user_service(db: Session = Depends(Database.get_db)) -> UserService:
    return UserService(db)