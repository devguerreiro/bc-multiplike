from fastapi import FastAPI

from app.controller.CompanyController import CompanyController

app = FastAPI()


@app.get("/companies")
async def list_companies():
    return "ok"
    # return CompanyController().list()
