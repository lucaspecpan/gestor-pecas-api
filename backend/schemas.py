from pydantic import BaseModel
from typing import Optional

# ===== Montadora =====
class MontadoraBase(BaseModel):
    nome: str

class MontadoraCreate(MontadoraBase):
    pass

class Montadora(MontadoraBase):
    id: int
    codigo: int

    class Config:
        from_attributes = True


# ===== Modelo =====
class ModeloBase(BaseModel):
    nome: int
    montadora_id: int

class ModeloCreate(ModeloBase):
    pass

class Modelo(ModeloBase):
    id: int
    codigo: str

    class Config:
        from_attributes = True


# ===== Porta =====
class PortaBase(BaseModel):
    nome: str

class PortaCreate(PortaBase):
    pass

class Porta(PortaBase):
    id: int

    class Config:
        from_attributes = True


# ===== Peça =====
class PecaCreate(BaseModel):
    item: str
    descricao: Optional[str]
    codigo_oem: str
    tipo: str
    modelo_id: int
    porta_id: int
    ano_de: int
    ano_ate: int
    imagem_url: Optional[str]

class Peca(BaseModel):
    id: int
    sku: str
    item: str
    descricao: Optional[str]
    codigo_oem: str
    tipo: str
    ano_de: int
    ano_ate: int
    imagem_url: Optional[str]

    class Config:
        from_attributes = True
