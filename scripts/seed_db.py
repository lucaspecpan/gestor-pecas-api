from backend.database import SessionLocal, engine, Base
from backend.models.pecas import Peca

Base.metadata.create_all(engine)

db = SessionLocal()

pecas_iniciais = [
    Peca(montadora="Volkswagen", modelo="Golf MK4", sku="10201999", quantidade=3, imagem_url=""),
    Peca(montadora="Honda", modelo="Fit 1ª Gen", sku="10302199", quantidade=5, imagem_url="")
]

db.add_all(pecas_iniciais)
db.commit()
db.close()