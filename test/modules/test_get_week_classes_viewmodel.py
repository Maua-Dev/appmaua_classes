import pytest
from datetime import time

from src.domain.entities._class import Class
from src.helpers.errors.domain_errors import EntityError
from src.domain.enums.week_days_enum import WeekDayEnum
from src.domain.enums.class_type_enum import ClassTypeEnum
from src.domain.enums.degree_enum import DegreeEnum
from src.modules.get_week_classes.get_week_classes_viewmodel import WeekClassesViewModel, ClassViewModel


class Test_WeekClassViewModel:

    def test_viewmodel(self):
        _classes = self._classes = [Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 0,
                                          "ECM407 - redes de Computadores", "Everson Denis", "E02", 1, 1, "ECM"),
                                    Class(time(16, 50, 0, 0), time(18, 30, 0, 0), 1,
                                          "ECM401 - Banco de Dados", "Aparecido Freitas", "E01", 1, 1, "ECM"),
                                    Class(time(15, 0, 0, 0), time(16, 40, 0, 0), 2,
                                          "ECM231 - Engenharia de Software", "Ana Serra", "E02", 1, 1, "ECM"),
                                    Class(time(16, 50, 0, 0), time(18, 30, 0, 0), 3,
                                          "EFH113 - Empreendedorismo e Gestão", "Reynaldo Cunha", "U14", 1, 1, "ECM"),
                                    Class(time(18, 40, 0, 0), time(20, 20, 0, 0), 4,
                                          "ECM231 - Engenharia de Software", "Ana Serra", "U14", 0, 1, "ECM")
                                    ]
        _classVm = [ClassViewModel(_class) for _class in _classes]

        _weekClassVm = WeekClassesViewModel(_classVm)

        assert len(_weekClassVm._0) == 1
        assert len(_weekClassVm._2) == 1
        assert len(_weekClassVm._3) == 1
        assert len(_weekClassVm._4) == 1
        assert len(_weekClassVm._5) == 0
        assert len(_weekClassVm._6) == 0

        _weekClassDict = _weekClassVm.toDict()

        assert _weekClassDict["0"] == [{
            "initTime": "15:00:00",
            "endTime": "16:40:00",
            "dayOfWeek": 0,
            "subject": "ECM407 - Redes De Computadores",
            "professor": "Everson Denis",
            "place": "E02",
            "classType": 1,
            "classValue": 1,
            "degree": "Engenharia De Computação"
        }]
