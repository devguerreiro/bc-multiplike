from typing import List
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.infra.exceptions import BadRequestException, NotFoundException
from app.infra.sqlalchemy import get_db, engine, Base
from app.infra.repositories.company import CompanyRepository
from app.controller.company import CompanyController
from app.domain.schemas.company import (
    CompanyCreate,
    CompanyList,
    CompanyRetrieve,
    CompanyUpdate,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/companies", response_model=List[CompanyList])
def list_companies(db: Session = Depends(get_db)):
    return CompanyController(CompanyRepository(db)).list()


@app.get("/companies/{cnpj}", response_model=CompanyRetrieve)
def retrieve_company(cnpj: str, db: Session = Depends(get_db)):
    try:
        data = CompanyController(CompanyRepository(db)).retrieve(cnpj)
        if data:
            return data

        return NotFoundException("Company not found")
    except ValueError as e:
        return BadRequestException(e)


@app.post("/companies", status_code=201)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    try:
        CompanyController(CompanyRepository(db)).create(company)
    except ValueError as e:
        return BadRequestException(e)


@app.put("/companies/{company_id}", status_code=204)
def update_company(
    company_id: int,
    data: CompanyUpdate,
    db: Session = Depends(get_db),
):
    try:
        CompanyController(CompanyRepository(db)).update(company_id, data)
    except ValueError as e:
        return BadRequestException(e)


@app.delete("/companies/{company_id}", status_code=204)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    try:
        CompanyController(CompanyRepository(db)).delete(company_id)
    except ValueError as e:
        return BadRequestException(e)
