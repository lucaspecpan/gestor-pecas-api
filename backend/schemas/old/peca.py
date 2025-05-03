from pydantic import BaseModel
from typing import Optional, List
from app.schemas.variacao import VariacaoOut

class PecaBase(BaseModel):
    nome_item: str
    categoria: Optional[str]
    anos_aplicacao: Optional[str]
    posicao_porta: Optional[str]
    codigo_oem: Optional[str]
    custo_ultima_compra: float
    preco_venda: float
    quantidade_estoque: int
    modelo_id: int

class PecaCreate(PecaBase):
    pass

class PecaOut(PecaBase):
    id: int
    sku: str
    variacoes: List[VariacaoOut] = []

    class Config:
        from_attributes = True
