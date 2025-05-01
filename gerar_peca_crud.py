import os

BASE_DIR = "app"

arquivos = {
    "models/peca.py": """from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Peca(Base):
    __tablename__ = "pecas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    codigo_sku = Column(String, unique=True, nullable=False)
    preco = Column(Float, nullable=False)
    montadora_id = Column(Integer, ForeignKey("montadoras.id"), nullable=False)
""",

    "schemas/peca.py": """from pydantic import BaseModel

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
""",

    "routers/peca.py": """from fastapi import APIRouter, Request, Depends, Form, status
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
""",

    "templates/pecas/listar.html": """<!DOCTYPE html>
<html>
<head>
    <title>Peças</title>
</head>
<body>
    <h1>Peças Cadastradas</h1>
    <a href="/pecas/nova">➕ Nova Peça</a>
    <ul>
        {% for peca in pecas %}
            <li>{{ peca.codigo_sku }} - {{ peca.nome }} - R$ {{ peca.preco }}</li>
        {% endfor %}
    </ul>
</body>
</html>
""",

    "templates/pecas/cadastrar.html": """<!DOCTYPE html>
<html>
<head>
    <title>Nova Peça</title>
</head>
<body>
    <h1>Cadastrar Peça</h1>
    <form method="post" action="/pecas">
        <label>Nome:</label>
        <input type="text" name="nome" required><br>
        <label>Preço:</label>
        <input type="number" name="preco" step="0.01" required><br>
        <label>Montadora:</label>
        <select name="montadora_id">
            {% for montadora in montadoras %}
                <option value="{{ montadora.id }}">{{ montadora.nome }}</option>
            {% endfor %}
        </select><br>
        <button type="submit">Cadastrar</button>
    </form>
</body>
</html>
"""
}

for caminho, conteudo in arquivos.items():
    caminho_completo = os.path.join(BASE_DIR, *caminho.split("/"))
    os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write(conteudo.strip())

print("✅ Arquivos do CRUD de Peças gerados com sucesso.")