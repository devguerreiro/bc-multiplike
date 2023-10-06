from abc import ABC
from typing import List

from app.domain.entity.company import Company


class CompanyRepository(ABC):
    def list(self) -> List[Company]:
        pass
