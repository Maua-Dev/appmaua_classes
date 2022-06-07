import pytest
from datetime import time, timezone, timedelta

from src.domain.entities.student import Student
from src.infra.repositories.class_repository_mock import ClassRepositoryMock
from src.domain.entities._class import Class
from src.domain.entities.professor import Professor


class Test_ClassRepositoryMock:

    def test_repository(self):
        repo: ClassRepositoryMock = ClassRepositoryMock()
        _class = Class(time(16, 50, 0, 0, timezone(timedelta(hours=-3))), time(18, 30, 0, 0, timezone(timedelta(hours=-3))), 1,
                       "EFH113 - Empreendedorismo e Gestão",
                       Professor("Reynaldo Cunha", "reynaldo@email.com", "999999999"),
                       "U14", 1, 1, "ECM")
        _student: Student = Student("Renan Reschke", "19020090", repo._classes)

        assert _class in repo._classes
        assert _student in repo._students

    @pytest.mark.asyncio
    async def test_get_student_week_classes(self):
        repo: ClassRepositoryMock = ClassRepositoryMock()

        _classes = await repo.get_student_week_classes("19020090")

        assert len(_classes) == 5
