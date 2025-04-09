from src.dto.UserDTO import UserDTO
from src.model.User import User
import json

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