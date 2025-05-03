# backend/models/pecas.py
from database import Base
from sqlalchemy import Column, Integer, String

class Peca(Base):
    __tablename__ = 'pecas'

    id = Column(Integer, primary_key=True, index=True)
    montadora = Column(String, index=True)
    modelo = Column(String, index=True)
    sku = Column(String, unique=True, index=True)
    quantidade = Column(Integer)
    imagem_url = Column(String)