from datetime import time

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.domain.enums.week_days_enum import WeekDayEnum
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum

class ClassDynamoDTO:
    initTime: str
    endTime: str
    dayOfWeek: int
    subject: dict
    place: str
    classType: int
    classValue: int
    degree: str

    def __init__(self, **kwargs):
        self.initTime = str(kwargs.get("initTime"))
        self.endTime = str(kwargs.get("endTime"))
        self.dayOfWeek = int(kwargs.get("dayOfWeek"))
        self.subject = kwargs.get("subject")
        self.place = str(kwargs.get("place"))
        self.classType = int(kwargs.get("classType"))
        self.classValue = int(kwargs.get("classValue"))
        self.degree = str(kwargs.get("degree"))

    @staticmethod
    def parseTime(isoformat: str) -> time:
        """
        :param isoformat: provided from dynamo (isoformat "HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]")
        :return: time
        """
        return time.fromisoformat(isoformat)

    @staticmethod
    def fromDynamo(data: dict):
        return ClassDynamoDTO(
            initTime=data.get("initTime"),
            endTime=data.get("endTime"),
            dayOfWeek=data.get("dayOfWeek"),
            subject=dict(
                code=data.get("subjectCode"),
                name=data.get("subjectName"),
                professor=dict(
                    email=data.get("professor").get("email"),
                    name=data.get("professor").get("name"),
                    phoneNumber=data.get("professor").get("phoneNumber")
                )
            ),
            place=data.get("place"),
            classType=data.get("classType"),
            classValue=data.get("classValue"),
            degree=data.get("degreeCode")
        )

    @staticmethod
    def fromEntity(entity: Class):
        return ClassDynamoDTO(
            initTime=str(entity.initTime.isoformat(timespec='microseconds')),
            endTime=str(entity.endTime.isoformat(timespec='microseconds')),
            dayOfWeek=int(entity.dayOfWeek.value),
            subject=dict(
                code=str(entity.subject.code),
                name=str(entity.subject.name),
                professor=dict(
                    email=str(entity.subject.professor.email),
                    name=str(entity.subject.professor.name),
                    phoneNumber=str(entity.subject.professor.phoneNumber)
                )
            ),
            place=str(entity.place),
            classType=int(entity.classType.value),
            classValue=int(entity.classValue),
            degree=str(entity.degree.name)
        )

    def toEntity(self) -> Class:
        return Class(initTime=ClassDynamoDTO.parseTime(self.initTime),
                     endTime=ClassDynamoDTO.parseTime(self.endTime),
                     dayOfWeek=WeekDayEnum(self.dayOfWeek),
                     subject=Subject(code=self.subject.get("code"),
                                     name=self.subject.get("name"),
                                     professor=Professor(name=self.subject.get("professor").get("name"),
                                                         email=self.subject.get("professor").get("email"),
                                                         phoneNumber=self.subject.get("professor").get("phoneNumber"))),
                     place=self.place,
                     classType=ClassTypeEnum(self.classType),
                     classValue=self.classValue,
                     degree=DegreeEnum[self.degree])

    def toDynamo(self, studentRA: str) -> dict:
        return dict(
            dayOfWeek=self.dayOfWeek,
            degreeCode=self.degree,
            endTime=self.endTime,
            professor=dict(
                name=self.subject.get("professor").get("name"),
                email=self.subject.get("professor").get("email"),
                phoneNumber=self.subject.get("professor").get("phoneNumber")
            ),
            initTime=self.initTime,
            studentRA=studentRA,
            subjectCode=self.subject.get("code"),
            subjectName=self.subject.get("name"),
            classType=self.classType,
            classValue=self.classValue,
            place=self.place
        )
