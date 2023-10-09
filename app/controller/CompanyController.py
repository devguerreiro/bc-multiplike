from app.application.usecase.GetCompany import GetCompany
from app.application.usecase.ListCompanies import ListCompanies
from app.domain.repositories.CompanyRepository import ICompanyRepository

from app.utils import is_a_valid_cnpj


class CompanyController:
    def __init__(self, repo: ICompanyRepository):
        self.repo = repo

    def list(self):
        return ListCompanies(self.repo).handle()

    def get_company(self, cnpj: str):
        if is_a_valid_cnpj(cnpj):
            return GetCompany(self.repo).handle(cnpj)
        raise ValueError("Invalid company")
