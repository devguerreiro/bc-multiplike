from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.infra.repositories.CompanyRepository import CompanyRepository
from app.infra.sqlalchemy import get_db

from app.controller.CompanyController import CompanyController

app = FastAPI()


@app.get("/companies")
async def list_companies(db: Session = Depends(get_db)):
    data = CompanyController(CompanyRepository(db)).list()
    return data
