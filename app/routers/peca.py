from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.peca import Peca
from app.models.montadora import Montadora
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../templates"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/pecas", response_class=HTMLResponse)
def listar_pecas(request: Request, db: Session = Depends(get_db)):
    pecas = db.query(Peca).all()
    montadoras = db.query(Montadora).all()
    return templates.TemplateResponse("pecas/listar.html", {"request": request, "pecas": pecas, "montadoras": montadoras})

@router.get("/pecas/nova", response_class=HTMLResponse)
def nova_peca(request: Request, db: Session = Depends(get_db)):
    montadoras = db.query(Montadora).all()
    return templates.TemplateResponse("pecas/cadastrar.html", {"request": request, "montadoras": montadoras})

@router.post("/pecas", response_class=HTMLResponse)
def criar_peca(
    request: Request,
    nome: str = Form(...),
    preco: float = Form(...),
    montadora_id: int = Form(...),
    db: Session = Depends(get_db)
):
    codigo_sku = f"SKU-{montadora_id}-{nome[:3].upper()}"
    nova = Peca(nome=nome, preco=preco, montadora_id=montadora_id, codigo_sku=codigo_sku)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return RedirectResponse(url="/pecas", status_code=status.HTTP_303_SEE_OTHER)