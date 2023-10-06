from fastapi import FastAPI

from app.controller.CompanyController import CompanyController
from app.infra.repositories.CompanyRepository import CompanyRepository

app = FastAPI()


@app.get("/companies")
async def list_companies():
    return CompanyController(CompanyRepository()).list()
