from pydantic import BaseModel, validator

from src.helpers.errors.domain_errors import EntityError


class Student (BaseModel):
    name: str
    ra: str

    @validator('name')
    def name_not_empty(self, v: str) -> str:
        if len(v) == 0:
            raise EntityError('name')
        return v.title()

    @validator('ra')
    def ra_is_valid(self, v: str) -> str:
        if len(v) != 8:
            raise EntityError('ra')
        return v