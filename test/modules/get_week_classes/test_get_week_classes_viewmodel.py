from datetime import time, timezone, timedelta

from src.domain.entities._class import Class
from src.domain.entities.professor import Professor
from src.modules.get_week_classes.get_week_classes_viewmodel import WeekClassesViewModel, ClassViewModel


class Test_WeekClassViewModel:

    def test_viewmodel(self):
        _classes = self._classes = [Class(time(15, 0, 0, 0, timezone(timedelta(hours=-3))), time(16, 40, 0, 0, timezone(timedelta(hours=-3))), 0,
                                          "ECM407 - redes de Computadores",
                                          Professor("Everson Denis", "everson@email.com", "999999999"), "E02", 1, 1,
                                          "ECM"),
                                    Class(time(16, 50, 0, 0, timezone(timedelta(hours=-3))), time(18, 30, 0, 0, timezone(timedelta(hours=-3))), 1,
                                          "ECM401 - Banco de Dados",
                                          Professor("Aparecido Freitas", "aparecido@email.com", "999999999"), "E01", 1,
                                          1, "ECM"),
                                    Class(time(15, 0, 0, 0, timezone(timedelta(hours=-3))), time(16, 40, 0, 0, timezone(timedelta(hours=-3))), 2,
                                          "ECM231 - Engenharia de Software",
                                          Professor("Ana Serra", "ana@email.com", "999999999"), "E02", 1, 1, "ECM"),
                                    Class(time(16, 50, 0, 0, timezone(timedelta(hours=-3))), time(18, 30, 0, 0, timezone(timedelta(hours=-3))), 3,
                                          "EFH113 - Empreendedorismo e Gestão",
                                          Professor("Reynaldo Cunha", "reynaldo@email.com", "999999999"), "U14", 1, 1,
                                          "ECM"),
                                    Class(time(18, 40, 0, 0, timezone(timedelta(hours=-3))), time(20, 20, 0, 0, timezone(timedelta(hours=-3))), 4,
                                          "ECM231 - Engenharia de Software",
                                          Professor("Ana Serra", "ana@email.com", "999999999"), "U14", 0, 1, "ECM")
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
