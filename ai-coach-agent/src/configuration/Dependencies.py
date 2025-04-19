from fastapi import Request, Depends
from requests import Session

from src.configuration import Database
from src.service.AIAgentService import AIAgentService
from src.service.PlayerMetricService import PlayerMetricService
from src.service.TrainingService import TrainingService
from src.service.UserService import UserService

def get_ai_agent_service(request: Request,
                         db: Session = Depends(Database.get_db)) -> AIAgentService:
    return AIAgentService(request.app.state.llm_trained_model,request.app.state.llm_rank_model,db)


def get_user_service(db: Session = Depends(Database.get_db)) -> UserService:
    return UserService(db)

def get_metric_service(db: Session = Depends(Database.get_db)) -> PlayerMetricService:
    return PlayerMetricService(db)

def get_training_service(db: Session = Depends(Database.get_db)) -> TrainingService:
    return TrainingService(db)