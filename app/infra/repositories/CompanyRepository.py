from typing import List

from app.application.repositories.CompanyRepository import ICompanyRepository
from app.domain.entity.company import Company


class CompanyRepository(ICompanyRepository):
    def list(self) -> List[Company]:
        return []
