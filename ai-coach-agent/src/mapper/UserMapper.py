from typing import List

from src.dto.UserDTO import UserDTO
from src.dto.UserWrapperDTO import UserWrapperDTO
from src.model.User import User
import json

from src.requestDTO.UserRequestDTO import UserRequestDTO
from src.responseDTO.UserResponseDTO import UserResponseDTO


def user_to_userDTO(user:User) -> UserDTO:
    userDTO = UserDTO()
    userDTO.password = user.password
    userDTO.username = user.username
    userDTO.email = user.email
    userDTO.status = user.status
    userDTO.fullname = user.fullname
    userDTO.uuid = user.uuid
    userDTO.phone = user.phone
    return userDTO


def user_to_userResponseDTO(user:User) -> UserResponseDTO:
    userResponseDTO = UserResponseDTO()
    userResponseDTO.username = user.username
    userResponseDTO.email = user.email
    userResponseDTO.fullname = user.fullname
    userResponseDTO.uuid = user.uuid
    userResponseDTO.phone = user.phone
    return userResponseDTO

def users_to_userResponseDTOs(users:List[User]) -> List[UserResponseDTO]:
    userResponseDTOs = []
    for user in users:
        userResponseDTO = user_to_userResponseDTO(user)
        userResponseDTOs.append(userResponseDTO)
    return userResponseDTOs

def users_to_userDTOs(users:List[User]) -> List[UserDTO]:
    userDTOs = []
    for user in users:
        userDTO = user_to_userDTO(user)
        userDTOs.append(userDTO)
    return userDTOs

def userDTO_to_user(userDTO:UserDTO) -> User:
    user = User()
    user.password = userDTO.password
    user.username = userDTO.username
    user.email = userDTO.email
    user.status = userDTO.status
    user.fullname = userDTO.fullname
    user.uuid = userDTO.uuid
    user.phone = userDTO.phone
    return user

def userDTOs_to_users(userDTOs:List[UserDTO]) -> List[User]:
    users = []
    for userDTO in userDTOs:
        user = userDTO_to_user(userDTO)
        users.append(user)
    return users

def userRequestDTO_to_userDTO(userRequestDTO:UserRequestDTO) -> UserDTO:
    userDTO = UserDTO()
    userDTO.password = userRequestDTO.password
    userDTO.username = userRequestDTO.username
    userDTO.email = userRequestDTO.email
    userDTO.fullname = userRequestDTO.fullname
    userDTO.phone = userRequestDTO.phone
    return userDTO


def userDTO_to_json(user_dto: UserDTO) -> str:
    return json.dumps({
        "user": {
            "username": user_dto.username,
            "fullname": user_dto.fullname,
            "email": user_dto.email,
            "uuid": user_dto.uuid,
            "phone": user_dto.phone,
        }
    })

def userWrapperDTO_to_dict(user_wrapper_dtos: List[UserWrapperDTO]) -> dict:
    users_list = []

    for user_wrapper_dto in user_wrapper_dtos:
        user_dict = {
            "username": user_wrapper_dto.user.username,
            "fullname": user_wrapper_dto.user.fullname,
            "email": user_wrapper_dto.user.email,
            "uuid": user_wrapper_dto.user.uuid,
            "phone": user_wrapper_dto.user.phone,
            "rank": user_wrapper_dto.user.rank,
            "player_metrics": [],
            "player_trainings": []
        }

        for player_metric_dto in user_wrapper_dto.playerMetrics or []:
            user_dict["player_metrics"].append({
                "blood_oxygen_level": player_metric_dto.blood_oxygen_level,
                "body_temperature": player_metric_dto.body_temperature,
                "calories_burned": player_metric_dto.calories_burned,
                "create_date_time": str(player_metric_dto.create_date_time),
                "gait_analysis": player_metric_dto.gait_analysis,
                "gps_data": player_metric_dto.gps_data,
                "heart_rate": player_metric_dto.heart_rate,
                "heart_rate_variability": player_metric_dto.heart_rate_variability,
                "impact_collision_detection": player_metric_dto.impact_collision_detection,
                "jump_count": player_metric_dto.jump_count,
                "jump_height": player_metric_dto.jump_height,
                "muscle_oxygenation": player_metric_dto.muscle_oxygenation,
                "recovery_time_estimation": player_metric_dto.recovery_time_estimation,
                "repetition_count_load": player_metric_dto.repetition_count_load,
                "sleep_duration": player_metric_dto.sleep_duration,
                "sleep_quality": player_metric_dto.sleep_quality,
                "status": player_metric_dto.status,
                "step_count": player_metric_dto.step_count,
                "stress_level": player_metric_dto.stress_level,
                "user_uuid": player_metric_dto.user_uuid,
                "uuid": player_metric_dto.uuid,
                "vo_max": player_metric_dto.vo_max,
                "workout_duration": player_metric_dto.workout_duration,
                "workout_type": player_metric_dto.workout_type
            })

        for training_dto in user_wrapper_dto.trainings or []:
            user_dict["player_trainings"].append({
                "training": training_dto.training,
                "create_date_time": str(training_dto.create_date_time)
            })

        users_list.append(user_dict)

    return {"users": users_list}
