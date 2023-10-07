from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.company import Company


class ICompanyRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Company]:
        pass
