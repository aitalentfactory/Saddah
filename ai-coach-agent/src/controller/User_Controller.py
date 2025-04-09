from fastapi import APIRouter, Depends

from src.configuration.Dependencies import get_user_service
from src.responseDTO.UserLoginResponseDTO import UserLoginResponseDTO
from src.service.UserService import UserService

aiUser = APIRouter()


@aiUser.get("/login", response_model=UserLoginResponseDTO ,tags=["User Login"])
async def login(username:str, password:str,
                        userService: UserService = Depends(get_user_service)  # Use the singleton
                        ) -> UserLoginResponseDTO:

    return userService.login(username, password)