import pytest

from src.domain.entities.student import Student
from src.helpers.errors.domain_errors import EntityError


class Test_Student:

    def test_student(self):
        student = Student("Renan scheidt reschke", "19020090", [])

        assert student.name == "Renan Scheidt Reschke"

    def test_student_entity_error1(self):
        with pytest.raises(EntityError):
            Student("", "19020090", [])

    def test_student_entity_error2(self):
        with pytest.raises(EntityError):
            Student("Renan scheidt reschke", "", [])

    def test_student_entity_error3(self):
        with pytest.raises(EntityError):
            Student("Renan scheidt reschke", "1902009000000", [])
