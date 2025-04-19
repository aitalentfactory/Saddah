from typing import List

from sqlalchemy.orm import Session

from src.dto.UserDTO import UserDTO
from src.mapper.UserMapper import user_to_userDTO, userDTO_to_json, userDTO_to_user, userRequestDTO_to_userDTO, \
    users_to_userResponseDTOs, users_to_userDTOs
from src.repository.UserRepository import UserRepository
from src.responseDTO.UserLoginResponseDTO import UserLoginResponseDTO
from src.service.PlayerMetricService import PlayerMetricService
from src.service.TrainingService import TrainingService
from src.util.CommonUtil import get_uuid


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.trainingService = TrainingService(db)
        self.playerMetricService = PlayerMetricService(db)

    def login(self,username,password):
        userLoginResponseDTO = UserLoginResponseDTO()
        user = self.repository.get_user_by_username(username)
        if user.username is not None:
            if user.password == password:
                userLoginResponseDTO.token = user.uuid
                userLoginResponseDTO.type = "Bearer"
                userLoginResponseDTO.expires = "1800"
            else:
                userLoginResponseDTO.isError = True
                userLoginResponseDTO.errorMessage = "Invalid Username or Password"
        else:
            userLoginResponseDTO.isError = True
            userLoginResponseDTO.errorMessage = "Invalid Username or Password"

        return userLoginResponseDTO

    def get_user_by_name(self, name):
        uppercase_name = name.upper()
        user = self.repository.get_user_by_name(uppercase_name)
        userDTO = user_to_userDTO(user)
        return userDTO

    def get_users(self):
        users = self.repository.get_users()
        userResponseDTOs = users_to_userResponseDTOs(users)
        return userResponseDTOs

    def get_users_dtos(self) -> List[UserDTO]:
        users = self.repository.get_users()
        userDTOs = users_to_userDTOs(users)
        return userDTOs

    def get_user_by_uuid(self, uuid):
        user = self.repository.get_user_by_uuid(uuid)
        userDTO = user_to_userDTO(user)
        return userDTO

    def register_user(self, userRequestDTO):
        userLoginResponseDTO = UserLoginResponseDTO()
        user = self.repository.get_user_by_username(userRequestDTO.username)
        if user.username is not None:
            userLoginResponseDTO.isError = True
            userLoginResponseDTO.errorMessage = "Username already exists"
        else:
            userDTO = userRequestDTO_to_userDTO(userRequestDTO)
            userDTO.uuid = get_uuid()
            userDTO.status = "V"
            user = userDTO_to_user(userDTO)
            seqID = self.repository.insert_user(user)
            if seqID is not None:
                userLoginResponseDTO.isError = False
                userLoginResponseDTO.errorMessage = "User Registration Successful"
            else:
                userLoginResponseDTO.isError = True
                userLoginResponseDTO.errorMessage = "User Registration Failed"
        return userLoginResponseDTO

    def convert_user_to_json(self,userDTO):
        userJson = userDTO_to_json(userDTO)
        return userJson