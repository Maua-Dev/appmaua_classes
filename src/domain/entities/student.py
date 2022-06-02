from pydantic import BaseModel, validator

from src.helpers.errors.domain_errors import EntityError


class Student (BaseModel):
    name: str
    ra: str

    @validator('name')
    def name_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('name')
        return v.title()

    @validator('ra')
    def ra_is_valid(cls, v: str) -> str:
        if len(v) != 8:
            raise EntityError('ra')
        return v

    def __init__(self, name: str, ra: str):
        super().__init__(name=name, ra=ra)
