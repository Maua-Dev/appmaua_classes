from pydantic import BaseModel, validator
from datetime import time

from src.helpers.errors.domain_errors import EntityError
from .professor import Professor
from ..enums.week_days_enum import WeekDayEnum
from ..enums.class_type_enum import ClassTypeEnum
from ..enums.degree_enum import DegreeEnum


class Class(BaseModel):
    initTime: time
    endTime: time
    dayOfWeek: WeekDayEnum
    subject: str
    professor: Professor
    place: str
    classType: ClassTypeEnum
    classValue: int
    degree: DegreeEnum

    @validator('endTime')
    def endTime_not_greater_than_init(cls, v: time, values) -> time:
        if 'initTime' in values and v < values['initTime']:
            raise EntityError('endTime')
        return v

    @validator('subject')
    def subject_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('subject')
        return v[0:6].upper() + v[6:].title()

    @validator('place')
    def place_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('place')
        return v.title()

    @validator('classValue')
    def classValue_is_valid(cls, v: int) -> int:
        if v < 1:
            raise EntityError('classValue')
        return v

