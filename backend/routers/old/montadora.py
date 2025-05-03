from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.montadora import Montadora
from app.schemas.montadora import MontadoraCreate
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../templates"))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/montadoras", response_class=HTMLResponse)
def listar_montadoras(request: Request, db: Session = Depends(get_db)):
    montadoras = db.query(Montadora).all()
    return templates.TemplateResponse("montadoras/listar.html", {"request": request, "montadoras": montadoras})

@router.get("/montadoras/nova", response_class=HTMLResponse)
def nova_montadora(request: Request):
    return templates.TemplateResponse("montadoras/cadastrar.html", {"request": request})

@router.post("/montadoras", response_class=HTMLResponse)
def criar_montadora(
    request: Request,
    nome: str = Form(...),
    sigla: str = Form(...),
    db: Session = Depends(get_db)
):
    nova = Montadora(nome=nome, sigla=sigla)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return RedirectResponse(url="/montadoras", status_code=status.HTTP_303_SEE_OTHER)
