from datetime import time, timezone, timedelta

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.week_days_enum import WeekDayEnum
from src.modules.get_week_classes.get_week_classes_viewmodel import WeekClassesViewModel, ClassViewModel


class Test_WeekClassViewModel:

    def test_viewmodel(self):
        _classes = self._classes = [Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                                          endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))),
                                          dayOfWeek=WeekDayEnum.SEGUNDA,
                                          subject="ECM407 - redes de Computadores",
                                          professor=Professor(name="Everson Denis", email="everson@email.com",
                                                              phoneNumber="999999999"),
                                          place="E02", classType=ClassTypeEnum.TURMA, classValue=1,
                                          degree=DegreeEnum.ECM),
                                    Class(initTime=time(16, 50, 0, 0, timezone(timedelta(hours=-3))),
                                          endTime=time(18, 30, 0, 0, timezone(timedelta(hours=-3))),
                                          dayOfWeek=WeekDayEnum.TERCA,
                                          subject="ECM401 - Banco de Dados",
                                          professor=Professor(name="Aparecido Freitas", email="aparecido@email.com",
                                                              phoneNumber="999999999"),
                                          place="E01", classType=ClassTypeEnum.TURMA, classValue=1,
                                          degree=DegreeEnum.ECM),
                                    Class(initTime=time(15, 0, 0, 0, timezone(timedelta(hours=-3))),
                                          endTime=time(16, 40, 0, 0, timezone(timedelta(hours=-3))),
                                          dayOfWeek=WeekDayEnum.QUARTA,
                                          subject="ECM231 - Engenharia de Software",
                                          professor=Professor(name="Ana Serra", email="ana@email.com",
                                                              phoneNumber="999999999"),
                                          place="E02", classType=ClassTypeEnum.TURMA, classValue=1,
                                          degree=DegreeEnum.ECM),
                                    Class(initTime=time(16, 50, 0, 0, timezone(timedelta(hours=-3))),
                                          endTime=time(18, 30, 0, 0, timezone(timedelta(hours=-3))),
                                          dayOfWeek=WeekDayEnum.QUINTA,
                                          subject="EFH113 - Empreendedorismo e Gestão",
                                          professor=Professor(name="Reynaldo Cunha", email="reynaldo@email.com",
                                                              phoneNumber="999999999"),
                                          place="U14", classType=ClassTypeEnum.TURMA, classValue=1,
                                          degree=DegreeEnum.ECM),
                                    Class(initTime=time(18, 40, 0, 0, timezone(timedelta(hours=-3))),
                                          endTime=time(20, 20, 0, 0, timezone(timedelta(hours=-3))),
                                          dayOfWeek=WeekDayEnum.SEXTA,
                                          subject="ECM231 - Engenharia de Software",
                                          professor=Professor(name="Ana Serra", email="ana@email.com",
                                                              phoneNumber="999999999"),
                                          place="U14", classType=ClassTypeEnum.GRUPO, classValue=1,
                                          degree=DegreeEnum.ECM)
                                    ]

        _weekClassVm = WeekClassesViewModel(_classes)

        assert len(_weekClassVm._0) == 1
        assert len(_weekClassVm._1) == 1
        assert len(_weekClassVm._2) == 1
        assert len(_weekClassVm._3) == 1
        assert len(_weekClassVm._4) == 1
        assert len(_weekClassVm._5) == 0
        assert len(_weekClassVm._6) == 0

        _weekClassDict = _weekClassVm.toDict()

        assert _weekClassDict["0"] == [{
            "initTime": "15:00:00-03:00",
            "endTime": "16:40:00-03:00",
            "dayOfWeek": 0,
            "subject": "ECM407 - Redes De Computadores",
            "professor": {"name": "Everson Denis",
                          "email": "everson@email.com",
                          "phoneNumber": "999999999"},
            "place": "E02",
            "classType": 1,
            "classValue": 1,
            "degree": "Engenharia De Computação"
        }]
