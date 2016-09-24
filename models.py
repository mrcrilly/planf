
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float

engine = create_engine("sqlite:///planf.sqlit3.db", echo=True)
session = sessionmaker(bind=engine)
base = declarative_base()

class Household(base):
    __tablename__ = "households"

    id = Column(Integer, primary_key=True)
    email_address = Column(String(100), nullable=False, unique=True)
    incomes = relationship("Income")
    savings = relationship("Saving")
    debts = relationship("Debt")
    expenses = relationship("Expense")

class Income(base):
    __tablename__ = "incomes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, default=0.0)
    household_id = Column(Integer, ForeignKey("households.id"))
    household = relationship("Household", back_populates="incomes")

class Saving(base):
    __tablename__ = "savings"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, default=0.0)
    household_id = Column(Integer, ForeignKey("households.id"))
    household = relationship("Household", back_populates="savings")

class Debt(base):
    __tablename__ = "debts"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, default=0.0)
    household_id = Column(Integer, ForeignKey("households.id"))
    household = relationship("Household", back_populates="debts")

class Expense(base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Float, default=0.0)
    household_id = Column(Integer, ForeignKey("households.id"))
    household = relationship("Household", back_populates="expenses")