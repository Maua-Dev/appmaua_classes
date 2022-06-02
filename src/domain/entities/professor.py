from pydantic import BaseModel, validator

from src.helpers.errors.domain_errors import EntityError


class Professor(BaseModel):
    name: str
    email: str
    phoneNumber: str

    @validator('name')
    def name_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('name')
        return v.title()

    @validator('email')
    def email_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('email')
        return v

    @validator('phoneNumber')
    def phoneNumber_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('phoneNumber')
        return v
