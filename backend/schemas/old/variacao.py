from pydantic import BaseModel
from typing import Optional

class VariacaoBase(BaseModel):
    tipo_variacao: str  # P ou R
    custo_total: float
    observacoes: Optional[str] = None

class VariacaoCreate(VariacaoBase):
    peca_id: int

class VariacaoOut(VariacaoBase):
    id: int

    class Config:
        from_attributes = True
