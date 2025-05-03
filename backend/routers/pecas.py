from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.pecas import Peca
from schemas.pecas import PecaCreate, PecaResponse

router = APIRouter(prefix="/pecas", tags=["Peças"])

@router.post("/", response_model=PecaResponse)
def create_peca(peca: PecaCreate, db: Session = Depends(get_db)):
    nova_peca = Peca(**peca.dict())
    db.add(nova_peca)
    db.commit()
    db.refresh(nova_peca)
    return nova_peca

@router.get("/", response_model=list[PecaResponse])
def listar_pecas(db: Session = Depends(get_db)):
    return db.query(Peca).all()