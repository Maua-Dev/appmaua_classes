from typing import List
from datetime import time

from src.domain.entities._class import Class
from src.domain.entities.student import Student
from src.domain.repositories.class_repository_interface import IClassRepository


class ClassRepositoryMock (IClassRepository):

    _classes: List[Class]
    _students: List[Student]

    def __init__(self):
        self._classes = [Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                               "ECM407 - redes de Computadores", "Everson Denis", "E02", 1, 1, "ECM"),
                         Class(time(16, 50, 0, 0), time(18, 30, 0, 0), 0,
                               "ECM401 - Banco de Dados", "Aparecido Freitas", "E01", 1, 1, "ECM"),
                         Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 1,
                               "ECM231 - Engenharia de Software", "Ana Serra", "E02", 1, 1, "ECM"),
                         Class(time(16, 50, 0, 0), time(18, 30, 0, 0), 1,
                               "EFH113 - Empreendedorismo e Gestão", "Reynaldo Cunha", "U14", 1, 1, "ECM"),
                         Class(time(18, 40, 0, 0), time(20, 20, 0, 0), 1,
                               "ECM231 - Engenharia de Software", "Ana Serra", "U14", 0, 1, "ECM")
                         ]

        self._students = [Student("Renan Reschke", "19020090", self._classes)]

    async def get_student_week_classes(self, ra: str) -> List[Class]:
        for student in self._students:
            if ra == student.ra:
                return student.classes
        return None

