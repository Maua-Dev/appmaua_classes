import pytest
from typing import List

from src.domain.entities._class import Class
from src.infra.repositories.class_repository_mock import ClassRepositoryMock
from src.modules.get_week_classes.get_week_classes_usecase import GetWeekClassesUsecase


class Test_GetWeekClassesUsecase:

    @pytest.mark.asyncio
    async def test_usecase(self):
        repo = ClassRepositoryMock()
        uc = GetWeekClassesUsecase(repo)

        classes = await uc("19020090")

        assert len(classes) == len(repo._classes)
        assert type(classes) is list
        assert type(classes[0]) is Class
        assert repo._classes[0] in classes

