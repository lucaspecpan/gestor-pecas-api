from pydantic import BaseModel

class ModeloBase(BaseModel):
    nome: str
    cod_modelo: int
    montadora_id: int

class ModeloCreate(ModeloBase):
    pass

class ModeloOut(ModeloBase):
    id: int

    class Config:
        from_attributes = True

