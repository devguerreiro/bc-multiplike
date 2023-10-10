from typing import List

from app.domain.repositories.company import ICompanyRepository
from app.domain.entities.company import Company


class ListCompanies:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self) -> List[Company]:
        return self.repo.get_all()
