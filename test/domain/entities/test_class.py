import pytest
from datetime import time, timezone, timedelta

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.helpers.errors.domain_errors import EntityError
from src.domain.enums.week_days_enum import WeekDayEnum
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum


class Test_Class:

    def test_class(self):
        _class = Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                       endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                       subject="Ecm407 - redes de ComPutadores",
                       professor=Professor(name="eVerson Denis", email="everson@email.com", phoneNumber="999999999"),
                       place="E02", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM)

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
            _class = Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                           endTime=time(13, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                           subject="Ecm407 - redes de ComPutadores",
                           professor=Professor(name="eVerson Denis", email="everson@email.com", phoneNumber="999999999"),
                           place="E02", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM)

    def test_class_entity_error2(self):
        with pytest.raises(EntityError):
            _class = Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                           endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                           subject="",
                           professor=Professor(name="eVerson Denis", email="everson@email.com", phoneNumber="999999999"),
                           place="E02", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM)

    def test_class_entity_error4(self):
        with pytest.raises(EntityError):
            _class = Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                           endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                           subject="",
                           professor=Professor(name="eVerson Denis", email="everson@email.com", phoneNumber="999999999"),
                           place="E02", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM)

    def test_class_entity_error5(self):
        with pytest.raises(EntityError):
            _class = Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                           endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                           subject="Ecm407 - redes de ComPutadores",
                           professor=Professor(name="eVerson Denis", email="everson@email.com", phoneNumber="999999999"),
                           place="", classType=ClassTypeEnum.TURMA, classValue=1, degree=DegreeEnum.ECM)

    def test_class_entity_error7(self):
        with pytest.raises(EntityError):
            _class = Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                           endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))), dayOfWeek=WeekDayEnum.SEGUNDA,
                           subject="Ecm407 - redes de ComPutadores",
                           professor=Professor(name="eVerson Denis", email="everson@email.com", phoneNumber="999999999"),
                           place="E02", classType=ClassTypeEnum.TURMA, classValue=-1, degree=DegreeEnum.ECM)
