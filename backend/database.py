import os
import psycopg2
from dotenv import load_dotenv

# Carrega variáveis do .env
load_dotenv()

DB_URL = os.getenv("SUPABASE_DB_URL")

# Força conexão segura com SSL
if DB_URL and "sslmode" not in DB_URL:
    DB_URL += "?sslmode=require"

# Conexão com banco Supabase
conn = psycopg2.connect(DB_URL)
