from sqlalchemy import Column, Integer, String
from app.database import Base

class Montadora(Base):
    __tablename__ = "montadoras"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False, unique=True)
    sigla = Column(String(10), nullable=False, unique=True)
