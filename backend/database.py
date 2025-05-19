import os
import psycopg2
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

DB_URL = os.getenv("SUPABASE_DB_URL")

# Conexão simples com Supabase PostgreSQL
conn = psycopg2.connect(DB_URL)

# Você pode usar conn.cursor() para executar queries diretas,
# ou usar SQLAlchemy se preferir (adaptamos depois)
