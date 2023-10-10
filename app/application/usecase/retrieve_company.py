from app.domain.repositories.company import ICompanyRepository
from app.domain.entities.company import Company

from app.utils import is_a_valid_cnpj


class RetrieveCompany:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self, cnpj: str) -> Company | None:
        if not is_a_valid_cnpj(cnpj):
            raise ValueError("Invalid company")

        return self.repo.get_by_cnpj(cnpj)
