import pytest

from src.domain.entities.student import Student
from src.helpers.errors.domain_errors import EntityError


class Test_Student:

    def test_student(self):
        student = Student(name="Renan scheidt reschke", ra="19020090", classes=[])

        assert student.name == "Renan Scheidt Reschke"

    def test_student_entity_error1(self):
        with pytest.raises(EntityError):
            Student(name="", ra="19020090", classes=[])

    def test_student_entity_error2(self):
        with pytest.raises(EntityError):
            Student(name="Renan scheidt reschke", ra="", classes=[])

    def test_student_entity_error3(self):
        with pytest.raises(EntityError):
            Student(name="Renan scheidt reschke", ra="1902009000000", classes=[])
