from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.infra.sqlalchemy import get_db, engine, Base
from app.infra.repositories.CompanyRepository import CompanyRepository
from app.controller.CompanyController import CompanyController
from app.domain.schemas.company import CompanyCreate

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/companies")
def list_companies(db: Session = Depends(get_db)):
    data = CompanyController(CompanyRepository(db)).list()
    return data


@app.get("/companies/{cnpj}")
def get_company(cnpj: str, db: Session = Depends(get_db)):
    try:
        data = CompanyController(CompanyRepository(db)).get_company(cnpj)
        if data:
            return data
        return JSONResponse(
            content={"error": "Company not found"},
            status_code=404,
        )
    except ValueError:
        return JSONResponse(
            content={"error": "Invalid CNPJ"},
            status_code=400,
        )


@app.post("/companies", status_code=201)
def add_company(company: CompanyCreate, db: Session = Depends(get_db)):
    try:
        CompanyController(CompanyRepository(db)).create(company)
    except ValueError as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=400,
        )
