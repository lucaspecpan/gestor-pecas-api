from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# ===== Montadora =====
class Montadora(Base):
    __tablename__ = 'montadoras'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)
    codigo = Column(Integer, unique=True)
    modelos = relationship("Modelo", back_populates="montadora")

# Sequência de código global para montadora
class MontadoraCodigoSeq(Base):
    __tablename__ = 'montadora_codigo_seq'
    id = Column(Integer, primary_key=True)
    valor_atual = Column(Integer, nullable=False, default=100)

# ===== Modelo =====
class Modelo(Base):
    __tablename__ = 'modelos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    codigo = Column(Integer)  # Gerado automaticamente
    montadora_id = Column(Integer, ForeignKey('montadoras.id'))
    montadora = relationship("Montadora", back_populates="modelos")

# Sequência de código por montadora
class ModeloCodigoSeq(Base):
    __tablename__ = 'modelo_codigo_seq'
    id = Column(Integer, primary_key=True)
    montadora_id = Column(Integer, unique=True)
    valor_atual = Column(Integer, nullable=False, default=1)

# ===== Porta =====
class Porta(Base):
    __tablename__ = 'portas'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)

# ===== Peça =====
class Peca(Base):
    __tablename__ = 'pecas'
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True)
    item = Column(String)
    descricao = Column(String)
    codigo_oem = Column(String)
    tipo = Column(String)
    porta_id = Column(Integer, ForeignKey('portas.id'))
    ano_de = Column(Integer)
    ano_ate = Column(Integer)
    imagem_url = Column(String)
    modelo_id = Column(Integer, ForeignKey('modelos.id'))
