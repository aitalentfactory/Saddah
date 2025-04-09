from typing import Optional

from pydantic import BaseModel, Field, field_validator


class AgentStateRequestDTO(BaseModel):
    message: str = Field(default=None, alias='message')
    gpt_mode: Optional[str] = 'KB'

    @field_validator('message', mode='before')
    def message_not_null(cls, v):
        if v is None or v == '':
            raise ValueError('message is required')
        return v

    def __str__(self):
        return self.model_dump_json(indent=4)