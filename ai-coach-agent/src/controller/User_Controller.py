from typing import List

from fastapi import APIRouter, Depends

from src.configuration.Dependencies import get_user_service, get_metric_service, get_training_service
from src.requestDTO.PlayerMetricRequestDTO import PlayerMetricRequestDTO
from src.requestDTO.UserRequestDTO import UserRequestDTO
from src.responseDTO.PlayerMetricResponseDTO import PlayerResponseMetricDTO
from src.responseDTO.TraningResponseDTO import TrainingResponseDTO
from src.responseDTO.UserLoginResponseDTO import UserLoginResponseDTO
from src.responseDTO.UserResponseDTO import UserResponseDTO
from src.service.PlayerMetricService import PlayerMetricService
from src.service.TrainingService import TrainingService
from src.service.UserService import UserService

aiUser = APIRouter()


@aiUser.get("/login", response_model=UserLoginResponseDTO ,tags=["User Login"])
async def login(username:str, password:str,
                        userService: UserService = Depends(get_user_service)  # Use the singleton
                        ) -> UserLoginResponseDTO:

    return userService.login(username, password)

@aiUser.post("/register", response_model=UserLoginResponseDTO ,tags=["User Register"])
async def register(userRequestDTO: UserRequestDTO,
                        userService: UserService = Depends(get_user_service)  # Use the singleton
                        ) -> UserLoginResponseDTO:

    return userService.register_user(userRequestDTO)

@aiUser.get("/players", response_model=List[UserResponseDTO] ,tags=["Get All Players"])
async def players(userService: UserService = Depends(get_user_service)  # Use the singleton
                        ) -> List[UserResponseDTO]:

    return userService.get_users()

@aiUser.get("/player_metrics", response_model=List[PlayerResponseMetricDTO] ,tags=["Get Player Metrics"])
async def get_player_metrics(player_uuid:str,
                   playerMetricService: PlayerMetricService = Depends(get_metric_service)  # Use the singleton
                        ) -> List[PlayerResponseMetricDTO]:

    return playerMetricService.get_latest_10_player_metrics_by_user_uuid_for_api_response(player_uuid)

@aiUser.post("/player_metric", response_model=PlayerResponseMetricDTO ,tags=["Create Player Metric"])
async def create_player_metric(player_metric_request_dto:PlayerMetricRequestDTO,
                   playerMetricService: PlayerMetricService = Depends(get_metric_service)  # Use the singleton
                        ) -> PlayerResponseMetricDTO:

    return playerMetricService.save(player_metric_request_dto)
@aiUser.get("/player_trainings", response_model=List[TrainingResponseDTO] ,tags=["Get Player Trainings"])
async def player_trainings(player_uuid:str,
                   trainingService: TrainingService = Depends(get_training_service)  # Use the singleton
                        ) -> List[TrainingResponseDTO]:

    return trainingService.get_latest_training_by_userUuid_api_response(player_uuid)