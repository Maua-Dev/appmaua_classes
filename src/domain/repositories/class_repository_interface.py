from abc import ABC, abstractmethod
from typing import List
from src.domain.entities._class import Class


class IClassRepository(ABC):

    @abstractmethod
    async def get_student_week_classes(self, ra: str) -> List[Class]:
        pass