from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Peca(Base):
    __tablename__ = "pecas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo_sku = Column(String, unique=True, nullable=False)
    preco = Column(Float, nullable=False)
    montadora_id = Column(Integer, ForeignKey("montadoras.id"), nullable=False)