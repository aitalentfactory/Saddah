from typing import Optional

from pydantic import BaseModel, Field

class TrainingResponseDTO(BaseModel):
    user_uuid: str = Field(default=None, alias='user_uuid')
    uuid: str = Field(default=None, alias='training_uuid')
    create_date_time: Optional[str] = Field(default=None, alias='create_date_time')
    training: str = Field(default=None, alias='training')