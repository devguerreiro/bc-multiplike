from app.application.repositories.CompanyRepository import CompanyRepository


class CompanyController:
    def init(self, repo: CompanyRepository = None):
        self.repo = repo

    def list(self):
        return self.repo.list()
