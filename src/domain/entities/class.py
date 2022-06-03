from pydantic import BaseModel, validator
from datetime import time

from src.helpers.errors.domain_errors import EntityError
from ..enums.week_days_enum import WeekDayEnum
from ..enums.class_type_enum import ClassTypeEnum
from ..enums.degree_enum import DegreeEnum


class Class(BaseModel):
    initTime: time
    endTime: time
    dayOfWeek: WeekDayEnum
    subject: str
    professor: str
    place: str
    classType: ClassTypeEnum
    classValue: int
    degree: DegreeEnum

    @validator('endTime')
    def endTime_not_greater_than_init(cls, v: time) -> time:
        if v < cls.initTime:
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

    @validator('professor')
    def professor_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('professor')
        return v.title()

    @validator('classValue')
    def classValue_is_valid(cls, v: int) -> int:
        if v < 1:
            raise EntityError('classValue')
        return v

    def __init__(self, initTime: time, endTime: time, dayOfWeek: int, subject: str,
                 professor: str, place: str, classType: int, classValue: int,
                 degree: str):
        """
            dayOfWeek - passar valor referente ao enum WeekDayEnum
            classType - passar valor referente ao enum ClassTypeEnum
            degree    - passar o codigo do curso do enum DegreeEnum
        """
        super().__init__(initTime=initTime, endTime=endTime, dayOfWeek=WeekDayEnum(dayOfWeek), subject=subject,
                         professor=professor, place=place, classType=ClassTypeEnum(classType),
                         classValue=classValue, degree=DegreeEnum[f'{degree}'])
