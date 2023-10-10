from datetime import datetime
from typing import List

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Float,
    Date,
    DateTime,
    Table,
)
from sqlalchemy.orm import relationship, Mapped

from app.infra.sqlalchemy import Base


CompanyCNAE = Table(
    "company_cnae",
    Base.metadata,
    Column("id", Integer, primary_key=True, index=True, autoincrement=True),
    Column("company_id", ForeignKey("company.id"), primary_key=True),
    Column("cnae_id", ForeignKey("cnae.id"), primary_key=True),
)


class CNAE(Base):
    __tablename__ = "cnae"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    description = Column(String(150))

    companies: Mapped[List["Company"]] = relationship(
        secondary=CompanyCNAE, back_populates="cnaes"
    )


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    cnpj = Column(String(14), unique=True, index=True)
    monthly_income = Column(Float)
    opened_date = Column(Date)
    created_at = Column(DateTime, default=datetime.now())

    cnaes: Mapped[List["CNAE"]] = relationship(
        secondary=CompanyCNAE, back_populates="companies"
    )
