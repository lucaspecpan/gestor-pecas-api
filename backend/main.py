from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import pecas
from database import engine, Base
import models.pecas

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(pecas.router)