from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Peca(Base):
    __tablename__ = "pecas"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    nome_item = Column(String, nullable=False)
    categoria = Column(String)
    anos_aplicacao = Column(String)
    posicao_porta = Column(String)
    codigo_oem = Column(String)
    custo_ultima_compra = Column(Float)
    preco_venda = Column(Float)
    quantidade_estoque = Column(Integer)
    modelo_id = Column(Integer, ForeignKey("modelos.id"))

    modelo = relationship("ModeloVeiculo", back_populates="pecas")
    variacoes = relationship("VariacaoPeca", back_populates="peca_base")
