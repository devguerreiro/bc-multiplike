from fastapi import Depends, FastAPI
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
