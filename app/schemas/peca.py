from pydantic import BaseModel

class PecaBase(BaseModel):
    nome: str
    codigo_sku: str
    preco: float
    montadora_id: int

class PecaCreate(PecaBase):
    pass

class PecaResponse(PecaBase):
    id: int

    class Config:
        from_attributes = True