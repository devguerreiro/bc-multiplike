from app.application.repositories.CompanyRepository import ICompanyRepository
from app.application.usecase.ListCompanies import ListCompanies


class CompanyController:
    def __init__(self, repo: ICompanyRepository):
        self.repo = repo

    def list(self):
        return ListCompanies(self.repo).handle()
