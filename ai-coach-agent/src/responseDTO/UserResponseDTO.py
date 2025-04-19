from pydantic import BaseModel, Field

class UserResponseDTO(BaseModel):
    uuid: str = Field(default=None, alias='uuid')
    username: str = Field(default=None, alias='username')
    email: str = Field(default=None, alias='email')
    fullname: str = Field(default=None, alias='fullname')
    phone: str = Field(default=None, alias='mobile')
    rank: float = Field(default=0.0, alias='rank')