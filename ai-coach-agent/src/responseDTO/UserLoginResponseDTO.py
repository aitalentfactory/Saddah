from pydantic import BaseModel, Field

class UserLoginResponseDTO(BaseModel):
    token: str  = Field(default=None, alias='token')
    type: str = Field(default=None, alias='type')
    expires: str = Field(default=None, alias='expires')
    isError: bool = Field(False, alias='is_error')
    errorMessage: str = Field(None, alias='error_message')

    def __str__(self):
        return self.model_dump_json(indent=4)