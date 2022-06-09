from pydantic import BaseModel, validator

from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError


class Subject (BaseModel):
    code: str
    name: str
    professor: Professor

    @validator('code')
    def code_is_valid(cls, v: str) -> str:
        if len(v) != 6:
            raise EntityError('code')
        return v.upper()

    @validator('name')
    def name_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('name')
        return v.title()