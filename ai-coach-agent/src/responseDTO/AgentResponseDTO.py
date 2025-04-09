from pydantic import BaseModel, Field

class AgentResponseDTO(BaseModel):
    playerName: str = Field(default=None, alias='player_name')
    playerReport: str = Field(default=None, alias='player_report')
    response: str = Field(default=None, alias='response')
    isError: bool = Field(False, alias='is_error')
    errorMessage: str = Field(None, alias='error_message')

    def __str__(self):
        return self.model_dump_json(indent=4)