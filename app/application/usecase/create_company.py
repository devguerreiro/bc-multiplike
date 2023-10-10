from app.domain.entities.company import Company
from app.domain.repositories.company import ICompanyRepository
from app.domain.schemas.company import CompanyCreate


class CreateCompany:
    def __init__(self, repo: ICompanyRepository) -> None:
        self.repo = repo

    def handle(self, company: CompanyCreate) -> None:
        if self.repo.get_by_cnpj(company.cnpj):
            raise ValueError("Company already exists")

        founded_cnaes = self.repo.get_cnaes_by_ids(company.cnaes)
        not_founded_cnaes = set(company.cnaes) - set(
            [cnae.id for cnae in founded_cnaes]
        )
        if not_founded_cnaes:
            raise ValueError(
                f"The following CNAEs are invalid: {not_founded_cnaes}",
            )

        new_company = Company(
            name=company.name,
            cnpj=company.cnpj,
            monthly_income=company.monthly_income,
            opened_date=company.opened_date,
            cnaes=founded_cnaes,
        )
        self.repo.insert(new_company)
