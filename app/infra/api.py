from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.infra.sqlalchemy import get_db, engine, Base
from app.infra.repositories.CompanyRepository import CompanyRepository
from app.controller.CompanyController import CompanyController

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/companies")
async def list_companies(db: Session = Depends(get_db)):
    data = CompanyController(CompanyRepository(db)).list()
    return data


@app.get("/companies/{cnpj}")
async def get_company(cnpj: str, db: Session = Depends(get_db)):
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
