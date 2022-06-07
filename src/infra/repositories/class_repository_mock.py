from typing import List
from datetime import time, timezone, timedelta

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.domain.entities.student import Student
from src.domain.repositories.class_repository_interface import IClassRepository


class ClassRepositoryMock (IClassRepository):

    _classes: List[Class]
    _students: List[Student]

    def __init__(self):
        self._classes = [Class(time(15, 0, 0, 0, timezone(timedelta(hours=-3))), time(16, 40, 0, 0, timezone(timedelta(hours=-3))), 0,
                               "ECM407 - redes de Computadores",
                               Professor("Everson Denis", "everson@email.com", "999999999"), "E02", 1, 1, "ECM"),
                         Class(time(16, 50, 0, 0, timezone(timedelta(hours=-3))), time(18, 30, 0, 0, timezone(timedelta(hours=-3))), 0,
                               "ECM401 - Banco de Dados",
                               Professor("Aparecido Freitas", "aparecido@email.com", "999999999"), "E01", 1, 1, "ECM"),
                         Class(time(15, 0, 0, 0, timezone(timedelta(hours=-3))), time(16, 40, 0, 0, timezone(timedelta(hours=-3))), 1,
                               "ECM231 - Engenharia de Software",
                               Professor("Ana Serra", "ana@email.com", "999999999"), "E02", 1, 1, "ECM"),
                         Class(time(16, 50, 0, 0, timezone(timedelta(hours=-3))), time(18, 30, 0, 0, timezone(timedelta(hours=-3))), 1,
                               "EFH113 - Empreendedorismo e Gestão",
                               Professor("Reynaldo Cunha", "reynaldo@email.com", "999999999"), "U14", 1, 1, "ECM"),
                         Class(time(18, 40, 0, 0, timezone(timedelta(hours=-3))), time(20, 20, 0, 0, timezone(timedelta(hours=-3))), 1,
                               "ECM231 - Engenharia de Software",
                               Professor("Ana Serra", "ana@email.com", "999999999"), "U14", 0, 1, "ECM")
                         ]

        self._students = [Student("Renan Reschke", "19020090", self._classes)]

    async def get_student_week_classes(self, ra: str) -> List[Class]:
        for student in self._students:
            if ra == student.ra:
                return student.classes
        return None

