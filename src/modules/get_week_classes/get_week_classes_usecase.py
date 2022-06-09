from typing import List

from src.domain.entities._class import Class
from src.domain.repositories.class_repository_interface import IClassRepository
from src.helpers.errors.domain_errors import NoItemsFound


class GetWeekClassesUsecase:
    def __init__(self, repo: IClassRepository):
        self._repo = repo

    async def __call__(self, ra: str) -> List[Class]:
        classes = await self._repo.get_student_week_classes(ra)

        if classes is None or len(classes) == 0:
            raise NoItemsFound('GetWeekClassesUsecase')

        return classes
