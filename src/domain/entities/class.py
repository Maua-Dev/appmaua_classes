from pydantic import BaseModel, validator
from datetime import time

from src.helpers.errors.domain_errors import EntityError
from ..enums.week_days_enum import WeekDayEnum
from ..enums.class_type_enum import ClassTypeEnum
from ..enums.degree_enum import DegreeEnum
from professor import Professor


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
    def endTime_not_greater_than_init(self, v: time) -> time:
        if v < self.initTime:
            raise EntityError('endTime')
        return v

    @validator('subject')
    def subject_is_not_empty(self, v: str) -> str:
        if len(v) == 0:
            raise EntityError('subject')
        return v[0:6].upper() + v[6:].title()

    @validator('place')
    def place_is_not_empty(self, v: str) -> str:
        if len(v) == 0:
            raise EntityError('place')
        return v.title()

    @validator('classValue')
    def classValue_is_valid(self, v: int) -> int:
        if v < 1:
            raise EntityError('classValue')
        return v

    def __init__(self, initTime: time, endTime: time, dayOfWeek: int, subject: str,
                 professor: Professor, place: str, classType: int, classValue: int,
                 degree: str):
        """
        dayOfWeek - passar valor referente ao enum WeekDayEnum
        classType - passar valor referente ao enum ClassTypeEnum
        degree    - passar o codigo do curso do enum DegreeEnum
        """
        self.initTime = initTime
        self.endTime = endTime
        self.dayOfWeek = WeekDayEnum(dayOfWeek)
        self.subject = subject
        self.professor = professor
        self.place = place
        self.classType = ClassTypeEnum(classType)
        self.classValue = classValue
        self.degree = DegreeEnum[f'{degree}']
