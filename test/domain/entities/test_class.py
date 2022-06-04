import pytest
from datetime import time

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError
from src.domain.enums.week_days_enum import WeekDayEnum
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum


class Test_Class:

    def test_class(self):
        _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                       "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                       "E02", 1, 1, "ECM")

        assert _class.initTime.hour == 15
        assert _class.endTime.minute == 40
        assert _class.dayOfWeek == WeekDayEnum.SEGUNDA
        assert _class.subject == "ECM407 - Redes De Computadores"
        assert _class.professor.name == "Everson Denis"
        assert _class.place == "E02"
        assert _class.classType == ClassTypeEnum.TURMA
        assert _class.degree == DegreeEnum.ECM

    def test_class_entity_error1(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(13, 40, 0, 0), 0,
                           "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                           "E02", 1, 1, "ECM")

    def test_class_entity_error2(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                           "", Professor("eVerson Denis", "everson@email.com", "999999999"), "E02", 1, 1, "ECM")

    def test_class_entity_error3(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 8,
                           "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                           "E02", 1, 1, "ECM")

    def test_class_entity_error4(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                           "", Professor("eVerson Denis", "everson@email.com", "999999999"), "E02", 1, 1, "ECM")

    def test_class_entity_error5(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                           "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                           "", 1, 1, "ECM")

    def test_class_entity_error6(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                           "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                           "E02", 6, 1, "ECM")

    def test_class_entity_error7(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                           "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                           "E02", 1, -1, "ECM")

    def test_class_entity_error8(self):
        with pytest.raises(EntityError):
            _class = Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                           "Ecm407 - redes de ComPutadores", Professor("eVerson Denis", "everson@email.com", "999999999"),
                           "E02", 1, 1, "EC")
