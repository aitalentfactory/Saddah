from sqlalchemy.orm import Session
from src.mapper.UserMapper import user_to_userDTO, userDTO_to_json
from src.repository.UserRepository import UserRepository
from src.responseDTO.UserLoginResponseDTO import UserLoginResponseDTO


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

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

    def get_user_by_uuid(self, uuid):
        user = self.repository.get_user_by_uuid(uuid)
        userDTO = user_to_userDTO(user)
        return userDTO

    def convert_user_to_json(self,userDTO):
        userJson = userDTO_to_json(userDTO)
        return userJson