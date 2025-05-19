cd
# create_db.py – Criação de tabelas com backend como pacote

from backend.database import Base, engine
from backend.models import Peca

print("📦 Criando as tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("✅ Tabelas criadas com sucesso.")
