from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def gerar_sku(db, modelo_id: int, tipo: str):
    modelo = db.query(models.Modelo).filter(models.Modelo.id == modelo_id).first()
    if not modelo:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")

    montadora = modelo.montadora
    prefixo = f"{montadora.codigo:03d}{modelo.codigo:02d}"

    total = db.query(models.Peca).filter(models.Peca.modelo_id == modelo_id).count()
    peca_num = 999 - total

    sufixo = ""
    tipo = tipo.lower()
    if tipo == "reparada":
        sufixo = "R"
    elif tipo == "patio":
        sufixo = "P"

    return f"{prefixo}{peca_num:03d}{sufixo}"


@router.post("/pecas/")
def criar_peca(peca: schemas.PecaCreate, db: Session = Depends(get_db)):
    sku = gerar_sku(db, peca.modelo_id, peca.tipo)
    nova = models.Peca(sku=sku, **peca.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/pecas/")
def listar_pecas(db: Session = Depends(get_db)):
    return db.query(models.Peca).all()
    
@router.get("/montadoras/")
def listar_montadoras(db: Session = Depends(get_db)):
    return db.query(models.Montadora).all()

@router.post("/modelos/")
def criar_modelo(modelo: schemas.ModeloCreate, db: Session = Depends(get_db)):
    modelos = db.query(models.Modelo).filter_by(montadora_id=modelo.montadora_id).count()
    codigo = f"{modelos+1:02d}"
    nova = models.Modelo(nome=modelo.nome, montadora_id=modelo.montadora_id, codigo=codigo)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/modelos/")
def listar_modelos(montadora_id: int, db: Session = Depends(get_db)):
    return db.query(models.Modelo).filter_by(montadora_id=montadora_id).all()

@router.post("/portas/")
def criar_porta(porta: schemas.PortaCreate, db: Session = Depends(get_db)):
    nova = models.Porta(**porta.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@router.get("/portas/")
def listar_portas(db: Session = Depends(get_db)):
    return db.query(models.Porta).all()
