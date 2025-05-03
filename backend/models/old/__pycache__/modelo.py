from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ModeloVeiculo(Base):
    __tablename__ = "modelos"

    id = Column(Integer, primary_key=True, index=True)
    cod_modelo = Column(Integer, index=True)
    nome = Column(String, nullable=False)
    montadora_id = Column(Integer, ForeignKey("montadoras.id"))

    montadora = relationship("Montadora", back_populates="modelos")
    pecas = relationship("Peca", back_populates="modelo")
