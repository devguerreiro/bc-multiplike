from typing import List

from sqlalchemy.orm import Session

from app.domain.repositories.company import ICompanyRepository
from app.domain.entities.company import CNAE, Company
from app.domain.schemas.company import CompanyUpdate


class CompanyRepository(ICompanyRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Company]:
        return self.db.query(Company).all()

    def get_by_cnpj(self, cnpj: str) -> Company | None:
        return self.db.query(Company).filter(Company.cnpj == cnpj).first()

    def insert(self, company: Company) -> None:
        self.db.add(company)
        self.db.commit()

    def get_cnaes_by_ids(self, ids: List[int]) -> List[CNAE]:
        return self.db.query(CNAE).filter(CNAE.id.in_(ids)).all()

    def update(
        self,
        company: Company,
        data: CompanyUpdate,
        cnaes: List[CNAE],
    ) -> None:
        company.name = data.name
        company.monthly_income = data.monthly_income
        company.opened_date = data.opened_date
        company.cnaes = cnaes
        self.db.commit()

    def get_by_id(self, id: int) -> Company | None:
        return self.db.query(Company).get(id)

    def delete(self, company: Company) -> None:
        self.db.delete(company)
        self.db.commit()
