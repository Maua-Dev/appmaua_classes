import pytest

from src.domain.enums.week_days_enum import WeekDayEnum
from src.infra.repositories.class_repository_mock import ClassRepositoryMock
from src.modules.get_week_classes.get_week_classes_usecase import GetWeekClassesUsecase
from src.modules.get_week_classes.get_week_classes_controller import GetWeekClassesController
from src.modules.get_week_classes.get_week_classes_viewmodel import WeekClassesViewModel
from src.helpers.http_models import HttpRequest, HttpResponse


class Test_GetWeekClassesController:
    repo = ClassRepositoryMock()
    uc = GetWeekClassesUsecase(repo)
    controller = GetWeekClassesController(uc)

    @pytest.mark.asyncio
    async def test_controller(self):
        retorno: HttpResponse = await self.controller(HttpRequest(query_params={"ra": "19020090"}))

        assert retorno.body["0"] == WeekClassesViewModel(self.repo._classes).toDict()["0"]

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
