from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routers import montadoras, modelos, pecas
from frontend.dash_app import create_dash_app
from starlette.middleware.wsgi import WSGIMiddleware

app = FastAPI()

# Permitir frontend acessar a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# Backend
app.include_router(montadoras.router)
app.include_router(modelos.router)
app.include_router(pecas.router)

# Frontend (Dash)
app.mount("/", WSGIMiddleware(create_dash_app()))
