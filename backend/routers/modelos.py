from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, cast, Integer
from backend import models, schemas
from backend.database import get_db
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/modelos", tags=["Modelos"])

@router.get("/", response_model=list[schemas.Modelo])
def listar_modelos(montadora_id: int = Query(...), db: Session = Depends(get_db)):
    return db.query(models.Modelo).filter_by(montadora_id=montadora_id).order_by(models.Modelo.nome).all()

@router.post("/", response_model=schemas.Modelo)
def criar_modelo(modelo: schemas.ModeloCreate, db: Session = Depends(get_db)):
    existente = db.query(models.Modelo).filter_by(nome=modelo.nome, montadora_id=modelo.montadora_id).first()
    if existente:
        raise HTTPException(status_code=400, detail="Modelo já existe para esta montadora.")

    # Busca maior código por montadora (string para int)
    maior_codigo = db.query(func.max(cast(models.Modelo.codigo, Integer))).filter_by(montadora_id=modelo.montadora_id).scalar()
    proximo_codigo = str((maior_codigo or 0) + 1).zfill(2)

    novo = models.Modelo(nome=modelo.nome, codigo=proximo_codigo, montadora_id=modelo.montadora_id)
    db.add(novo)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao inserir modelo. Código duplicado.")
    db.refresh(novo)
    return novo
