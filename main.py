# main.py
from fastapi import FastAPI
from backend.routers import montadoras

app = FastAPI()

# Incluir rotas
app.include_router(montadoras.router)
