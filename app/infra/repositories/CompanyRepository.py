from typing import List

from sqlalchemy.orm import Session

from app.domain.repositories.CompanyRepository import ICompanyRepository
from app.domain.entities.company import Company


class CompanyRepository(ICompanyRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Company]:
        return self.db.query(Company).all()
