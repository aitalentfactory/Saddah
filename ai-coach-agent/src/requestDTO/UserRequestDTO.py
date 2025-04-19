from pydantic import BaseModel, Field, field_validator


class UserRequestDTO(BaseModel):
    username: str = Field(default=None, alias='username')
    password: str = Field(default=None, alias='password')
    email: str = Field(default=None, alias='email')
    fullname: str = Field(default=None, alias='fullname')
    phone: str = Field(default=None, alias='mobile')

    @field_validator('username', mode='before')
    def username_not_null(cls, v):
        if v is None or v == '':
            raise ValueError('username is required')
        return v

    @field_validator('password', mode='before')
    def password_not_null(cls, v):
        if v is None or v == '':
            raise ValueError('password is required')
        return v

    @field_validator('email', mode='before')
    def email_not_null(cls, v):
        if v is None or v == '':
            raise ValueError('email is required')
        return v

    @field_validator('fullname', mode='before')
    def fullname_not_null(cls, v):
        if v is None or v == '':
            raise ValueError('fullname is required')
        return v

    @field_validator('phone', mode='before')
    def mobile_not_null(cls, v):
        if v is None or v == '':
            raise ValueError('mobile is required')
        return v

    def __str__(self):
        return self.model_dump_json(indent=4)
