from typing import List
from datetime import time

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.week_days_enum import WeekDayEnum


class ProfessorViewModel:
    name: str
    email: str
    phoneNumber: str

    def __init__(self, _professor: Professor):
        self.name = _professor.name
        self.email = _professor.email
        self.phoneNumber = _professor.phoneNumber

    def toDict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phoneNumber": self.phoneNumber
        }


class SubjectViewModel:
    code: str
    name: str
    professor: ProfessorViewModel

    def __init__(self, _subject: Subject):
        self.code = _subject.code
        self.name = _subject.name
        self.professor = ProfessorViewModel(_subject.professor)

    def toDict(self):
        return {
            "code": self.code,
            "name": self.name,
            "professor": self.professor.toDict()
        }

class ClassViewModel:
    initTime: time
    endTime: time
    dayOfWeek: WeekDayEnum
    subject: SubjectViewModel
    place: str
    classType: ClassTypeEnum
    classValue: int
    degree: DegreeEnum

    def __init__(self, _class: Class):
        self.initTime = _class.initTime
        self.endTime = _class.endTime
        self.dayOfWeek = _class.dayOfWeek
        self.subject = SubjectViewModel(_class.subject)
        self.place = _class.place
        self.classType = _class.classType
        self.classValue = _class.classValue
        self.degree = _class.degree

    def toDict(self):
        return {
            "initTime": self.initTime.isoformat(),
            "endTime": self.endTime.isoformat(),
            "dayOfWeek": self.dayOfWeek.value,
            "subject": self.subject.toDict(),
            "place": self.place,
            "classType": self.classType.value,
            "classValue": self.classValue,
            "degree": self.degree.value.title()
        }

class WeekClassesViewModel:
    _0: List[ClassViewModel]
    _1: List[ClassViewModel]
    _2: List[ClassViewModel]
    _3: List[ClassViewModel]
    _4: List[ClassViewModel]
    _5: List[ClassViewModel]
    _6: List[ClassViewModel]

    def __init__(self, _classes: List[Class]):

        classesVm = [ClassViewModel(_class) for _class in _classes]

        self._0 = [_class for _class in classesVm if _class.dayOfWeek.value == 0]
        self._1 = [_class for _class in classesVm if _class.dayOfWeek.value == 1]
        self._2 = [_class for _class in classesVm if _class.dayOfWeek.value == 2]
        self._3 = [_class for _class in classesVm if _class.dayOfWeek.value == 3]
        self._4 = [_class for _class in classesVm if _class.dayOfWeek.value == 4]
        self._5 = [_class for _class in classesVm if _class.dayOfWeek.value == 5]
        self._6 = [_class for _class in classesVm if _class.dayOfWeek.value == 6]

    def toDict(self):
        return {
            "0": [_class.toDict() for _class in self._0],
            "1": [_class.toDict() for _class in self._1],
            "2": [_class.toDict() for _class in self._2],
            "3": [_class.toDict() for _class in self._3],
            "4": [_class.toDict() for _class in self._4],
            "5": [_class.toDict() for _class in self._5],
            "6": [_class.toDict() for _class in self._6],
        }
