from pydantic import BaseModel

class MontadoraBase(BaseModel):
    nome: str
    sigla: str

class MontadoraCreate(MontadoraBase):
    pass

class MontadoraResponse(MontadoraBase):
    id: int

    class Config:
        from_attributes = True
