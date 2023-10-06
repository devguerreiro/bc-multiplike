from typing import List

from app.application.repositories.CompanyRepository import ICompanyRepository
from app.domain.entity.company import Company


class ListCompanies:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self) -> List[Company]:
        return self.repo.list()
