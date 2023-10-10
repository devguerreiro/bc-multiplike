from typing import List

from app.application.usecase.create_company import CreateCompany
from app.application.usecase.retrieve_company import RetrieveCompany
from app.application.usecase.list_companies import ListCompanies
from app.application.usecase.update_company import UpdateCompany
from app.domain.entities.company import Company
from app.domain.repositories.company import ICompanyRepository
from app.domain.schemas.company import CompanyCreate, CompanyUpdate


class CompanyController:
    def __init__(self, repo: ICompanyRepository):
        self.repo = repo

    def list(self) -> List[Company]:
        return ListCompanies(self.repo).handle()

    def retrieve(self, cnpj: str) -> Company | None:
        return RetrieveCompany(self.repo).handle(cnpj)

    def create(self, company: CompanyCreate) -> None:
        CreateCompany(self.repo).handle(company)

    def update(self, company_id: int, data: CompanyUpdate) -> None:
        UpdateCompany(self.repo).handle(company_id, data)
