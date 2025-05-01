from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Engine de conexão com o banco de dados
engine = create_engine(settings.DATABASE_URL)

# Criar a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()
