from app.domain.repositories.company import ICompanyRepository


class DeleteCompany:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self, company_id: int) -> None:
        company = self.repo.get_by_id(company_id)
        if not company:
            raise ValueError("Company does not exist")

        self.repo.delete(company)
