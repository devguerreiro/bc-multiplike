from datetime import datetime
from decimal import Decimal
from typing import List
from pydantic import BaseModel, Field, field_validator

from app.utils import is_a_valid_cnpj


class CompanyWrite(BaseModel):
    name: str = Field(
        min_length=5,
        max_length=100,
        description="Company's name",
    )
    monthly_income: Decimal = Field(
        decimal_places=2,
        description="Company's monthly income",
    )
    opened_date: str = Field(
        description="Company's opened date",
        pattern=r"\d{2}/\d{2}/\d{4}",
        examples=["dd/mm/yyyy"],
    )
    cnaes: List[int] = Field(description="Company's each CNAE id")

    @field_validator("opened_date")
    @classmethod
    def opened_date_must_be_in_br_format(cls, value: str):
        try:
            return datetime.strptime(value, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(
                "Invalid date format. Must be in dd/mm/yyyy format",
            )


class CompanyCreate(CompanyWrite):
    cnpj: str = Field(
        min_length=14,
        max_length=14,
        pattern=r"\d{14}",
        description="Company's CNPJ",
        examples=["12345678901234"],
    )

    @field_validator("cnpj")
    @classmethod
    def cnpj_must_be_a_valid_document(cls, value: str):
        if is_a_valid_cnpj(value):
            return value
        raise ValueError("Invalid document")


class CompanyUpdate(CompanyWrite):
    pass
