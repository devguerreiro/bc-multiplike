from typing import List
from datetime import date, datetime


class Company:
    id: int
    name: str
    cnpj: str
    cnae: List[str]
    monthly_income: float
    date: date
    registration_date: datetime
