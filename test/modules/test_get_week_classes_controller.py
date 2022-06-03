import pytest

from src.infra.repositories.class_repository_mock import ClassRepositoryMock
from src.modules.get_week_classes.get_week_classes_usecase import GetWeekClassesUsecase
from src.modules.get_week_classes.get_week_classes_controller import GetWeekClassesController
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.helpers.errors.controller_errors import MissingParameters
from src.helpers.errors.domain_errors import NoItemsFound


class Test_GetWeekClassesController:

    repo = ClassRepositoryMock()
    uc = GetWeekClassesUsecase(repo)
    controller = GetWeekClassesController(uc)

    @pytest.mark.asyncio
    async def test_controller(self):

        retorno: HttpResponse = await self.controller(HttpRequest(query_params={"ra": "19020090"}))

        assert retorno.body["0"] == [{
                                        "initTime": "15:00:00",
                                        "endTime": "16:40:00",
                                        "dayOfWeek": 0,
                                        "subject": "ECM407 - Redes De Computadores",
                                        "professor": "Everson Denis",
                                        "place": "E02",
                                        "classType": 1,
                                        "classValue": 1,
                                        "degree": "Engenharia De Computação"
                                    },
                                    {
                                        "initTime": "16:50:00",
                                        "endTime": "18:30:00",
                                        "dayOfWeek": 0,
                                        "subject": "ECM401 - Banco De Dados",
                                        "professor": "Aparecido Freitas",
                                        "place": "E01",
                                        "classType": 1,
                                        "classValue": 1,
                                        "degree": "Engenharia De Computação"
                                    }
                                    ]

    @pytest.mark.asyncio
    async def test_controller_error1(self):
        retorno: HttpResponse = await self.controller(HttpRequest(query_params={}))
        assert retorno.status_code == 400
        assert retorno.body["erro"] == "Field ra is missing."

    @pytest.mark.asyncio
    async def test_controller_error2(self):
        retorno: HttpResponse = await self.controller(HttpRequest(query_params={"ra": "18020090"}))
        assert retorno.status_code == 204
        assert retorno.body["erro"] == "Usecase GetWeekClassesUsecase have failed. No items found"

    @pytest.mark.asyncio
    async def test_controller_error3(self):
        retorno: HttpResponse = await self.controller(HttpRequest(query_params={"ra": ""}))
        assert retorno.status_code == 400
        assert retorno.body["erro"] == "Field ra is missing."

    @pytest.mark.asyncio
    async def test_controller_error4(self):
        retorno: HttpResponse = await self.controller(HttpRequest(query_params={"ra": 19020090}))
        assert retorno.status_code == 400
        assert retorno.body["erro"] == "Field ra has the wrong type (int). Correct type: str."