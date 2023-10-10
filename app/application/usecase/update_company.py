from app.domain.repositories.company import ICompanyRepository
from app.domain.schemas.company import CompanyUpdate


class UpdateCompany:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self, company_id: int, data: CompanyUpdate) -> None:
        company = self.repo.get_by_id(company_id)
        if not company:
            raise ValueError("Company does not exist")

        founded_cnaes = self.repo.get_cnaes_by_ids(data.cnaes)
        founded_cnaes_ids = [cnae.id for cnae in founded_cnaes]
        not_founded_cnaes_ids = set(data.cnaes) - set(founded_cnaes_ids)
        if not_founded_cnaes_ids:
            raise ValueError(
                f"The following CNAEs are invalid: {not_founded_cnaes_ids}",
            )

        self.repo.update(company, data, founded_cnaes)
