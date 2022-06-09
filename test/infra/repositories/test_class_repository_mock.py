import pytest
from datetime import time, timezone, timedelta

from src.domain.entities.student import Student
from src.domain.entities.subject import Subject
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.week_days_enum import WeekDayEnum
from src.infra.repositories.class_repository_mock import ClassRepositoryMock
from src.domain.entities._class import Class
from src.domain.entities.professor import Professor


class Test_ClassRepositoryMock:

    def test_repository(self):
        repo: ClassRepositoryMock = ClassRepositoryMock()
        _class = Class(initTime=time(16, 50, 0, 0, timezone(timedelta(hours=-3))),
                       endTime=time(18, 30, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.TERCA,
                       subject=Subject(code="EFH113", name="Empreendedorismo e Gestão",
                                       professor=Professor(name="Reynaldo Cunha",
                                                           email="reynaldo@email.com",
                                                           phoneNumber="999999999")),
                       place="U14", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM)
        _student: Student = Student(name="Renan Reschke", ra="19020090", classes=repo._classes)

        assert _class in repo._classes
        assert _student in repo._students

    @pytest.mark.asyncio
    async def test_get_student_week_classes(self):
        repo: ClassRepositoryMock = ClassRepositoryMock()

        _classes = await repo.get_student_week_classes("19020090")

        assert len(_classes) == len(repo._classes)
