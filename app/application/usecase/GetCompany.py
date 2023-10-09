from app.domain.repositories.CompanyRepository import ICompanyRepository
from app.domain.entities.company import Company


class GetCompany:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self, cnpj: str) -> Company:
        return self.repo.get_by_cnpj(cnpj)
