from pydantic import BaseModel, validator
from typing import List

from src.helpers.errors.domain_errors import EntityError
from ._class import Class


class Student (BaseModel):
    name: str
    ra: str
    classes: List[Class]

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
