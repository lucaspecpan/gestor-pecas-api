from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Montadora(Base):
    __tablename__ = "montadoras"

    id = Column(Integer, primary_key=True, index=True)
    cod_montadora = Column(Integer, unique=True, index=True)
    nome = Column(String, unique=True, nullable=False)

    modelos = relationship("ModeloVeiculo", back_populates="montadora")
