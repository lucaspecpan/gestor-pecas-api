from pydantic import BaseModel

class MontadoraBase(BaseModel):
    nome: str
    cod_montadora: int

class MontadoraCreate(MontadoraBase):
    pass

class MontadoraOut(MontadoraBase):
    id: int

    class Config:
        from_attributes = True

