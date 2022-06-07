from typing import List
from datetime import time, timezone, timedelta

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.domain.entities.student import Student
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.week_days_enum import WeekDayEnum
from src.domain.repositories.class_repository_interface import IClassRepository


class ClassRepositoryMock (IClassRepository):

    _classes: List[Class]
    _students: List[Student]

    def __init__(self):
        self._classes = [Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                               endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                               subject="ECM407 - redes de Computadores",
                               professor=Professor(name="Everson Denis", email="everson@email.com", phoneNumber="999999999"),
                               place="E02", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM),
                         Class(initTime=time(16, 50, 0, 0, timezone(timedelta(hours=-3))),
                               endTime=time(18, 30, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                               subject="ECM401 - Banco de Dados",
                               professor=Professor(name="Aparecido Freitas", email="aparecido@email.com", phoneNumber="999999999"),
                               place="E01", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM),
                         Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                               endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.TERCA,
                               subject="ECM231 - Engenharia de Software",
                               professor=Professor(name="Ana Serra", email="ana@email.com", phoneNumber="999999999"),
                               place="E02", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM),
                         Class(initTime=time(16, 50, 0, 0, timezone(timedelta(hours=-3))),
                               endTime=time(18, 30, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.TERCA,
                               subject="EFH113 - Empreendedorismo e Gestão",
                               professor=Professor(name="Reynaldo Cunha", email="reynaldo@email.com", phoneNumber="999999999"),
                               place="U14", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM),
                         Class(initTime=time(18, 40, 0, 0, timezone(timedelta(hours=-3))),
                               endTime=time(20, 20, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.TERCA,
                               subject="ECM231 - Engenharia de Software",
                               professor=Professor(name="Ana Serra", email="ana@email.com", phoneNumber="999999999"),
                               place="U14", classType=ClassTypeEnum.GRUPO, classValue=1, degree=DegreeEnum.ECM)
                         ]

        self._students = [Student(name="Renan Reschke", ra="19020090", classes=self._classes)]

    async def get_student_week_classes(self, ra: str) -> List[Class]:
        for student in self._students:
            if ra == student.ra:
                return student.classes
        return None

