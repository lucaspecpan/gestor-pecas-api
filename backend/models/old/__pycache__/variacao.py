from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class VariacaoPeca(Base):
    __tablename__ = "variacoes"

    id = Column(Integer, primary_key=True, index=True)
    tipo_variacao = Column(String, nullable=False)  # P ou R
    custo_total = Column(Float)
    observacoes = Column(String)
    peca_id = Column(Integer, ForeignKey("pecas.id"))

    peca_base = relationship("Peca", back_populates="variacoes")
