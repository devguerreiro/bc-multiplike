from app.application.usecase.ListCompanies import ListCompanies
from app.domain.repositories.CompanyRepository import ICompanyRepository


class CompanyController:
    def __init__(self, repo: ICompanyRepository):
        self.repo = repo

    def list(self):
        return ListCompanies(self.repo).handle()
