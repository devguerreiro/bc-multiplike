from abc import ABC, abstractmethod
from typing import List

from app.domain.entities.company import CNAE, Company
from app.domain.schemas.company import CompanyUpdate


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

    @abstractmethod
    def update(self, company: Company, data: CompanyUpdate) -> None:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Company | None:
        pass
