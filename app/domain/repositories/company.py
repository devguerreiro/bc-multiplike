from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.company import CNAE, Company


class ICompanyRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Company]:
        pass

    @abstractmethod
    def get_by_cnpj(self, cnpj: str) -> Company | None:
        pass

    @abstractmethod
    def insert(self, company: Company) -> None:
        pass

    @abstractmethod
    def get_cnaes_by_ids(self, ids: List[int]) -> List[CNAE]:
        pass
