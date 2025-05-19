import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from backend.models import Base, Montadora, Modelo, Peca, Porta

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def gerar_sku(montadora: Montadora, modelo: Modelo, numero: int, tipo: str):
    sufixo = ""
    if tipo == "reparada":
        sufixo = "R"
    elif tipo == "patio":
        sufixo = "P"
    return f"{montadora.codigo}{modelo.codigo}{numero:03d}{sufixo}"

def main():
    # ⚠️ Apaga tudo antes de criar
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    montadoras = {
        "HYUNDAI": "101",
        "VOLKSWAGEN": "102",
        "KIA": "103",
        "HONDA": "104"
    }

    montadora_objs = {}
    for nome, codigo in montadoras.items():
        m = Montadora(nome=nome, codigo=codigo)
        db.add(m)
        db.commit()
        montadora_objs[nome] = m

    modelos_data = {
        ("HYUNDAI", "SANTA FÉ"): "01",
        ("KIA", "SORENTO"): "01",
        ("VOLKSWAGEN", "GOLF MK4"): "01",
        ("HONDA", "FIT"): "01"
    }

    modelo_objs = {}
    for (mont_nome, modelo_nome), codigo in modelos_data.items():
        modelo = Modelo(nome=modelo_nome, codigo=codigo, montadora_id=montadora_objs[mont_nome].id)
        db.add(modelo)
        db.commit()
        modelo_objs[(mont_nome, modelo_nome)] = modelo

    portas = set()
    pecas = [
        ("HYUNDAI", "SANTA FÉ", "83470-2B020J4S4", "TE/RL", "normal", 999, 2007, 2012, 1),
        ("KIA", "SORENTO", "82402-2P001", "DD/FR", "normal", 999, 2009, 2014, 2),
        ("KIA", "SORENTO", "82401-2P001", "DE/FL", "normal", 998, 2009, 2014, 1),
        ("KIA", "SORENTO", "82401-2P001", "DE/FL", "patio", 998, 2009, 2014, 1),
        ("KIA", "SORENTO", "83401-2P000", "TE/RL", "normal", 996, 2009, 2014, 1),
        ("KIA", "SORENTO", "83402-2P000", "TD/RR", "normal", 997, 2009, 2014, 1),
        ("VOLKSWAGEN", "GOLF MK4", "1J4 839 756 E", "TD/RR", "normal", 999, 1998, 2007, 9),
        ("VOLKSWAGEN", "GOLF MK4", "1J4 839 756 E", "TD/RR", "reparada", 999, 1998, 2007, 1),
        ("VOLKSWAGEN", "GOLF MK4", "1139", "LD", "normal", 996, 1998, 2007, 1),
        ("VOLKSWAGEN", "GOLF MK4", "1J4 839 755 E", "TE/RL", "normal", 998, 1998, 2007, 11),
        ("VOLKSWAGEN", "GOLF MK4", "1138", "LE", "normal", 997, 1998, 2007, 1),
        ("HONDA", "FIT", "130821975", "TD/RR", "normal", 999, 2003, 2008, 1)
    ]

    for mont, mod, oem, porta, tipo, numero, ano_de, ano_ate, estoque in pecas:
        modelo = modelo_objs[(mont, mod)]
        montadora = montadora_objs[mont]
        portas.add(porta)

        p = Peca(
            sku=gerar_sku(montadora, modelo, numero, tipo),
            item=f"{mod} {porta}",
            descricao=None,
            codigo_oem=oem,
            tipo=tipo,
            modelo_id=modelo.id,
            porta_id=None,
            ano_de=ano_de,
            ano_ate=ano_ate,
            imagem_url=None
        )
        db.add(p)

    db.commit()

    porta_map = {}
    for nome in portas:
        obj = Porta(nome=nome)
        db.add(obj)
        db.commit()
        porta_map[nome] = obj.id

    pecas = db.query(Peca).all()
    for p in pecas:
        for porta in porta_map:
            if porta in p.item:
                p.porta_id = porta_map[porta]
    db.commit()

    db.close()
    print("✅ Banco de dados (Neon) populado com sucesso!")

if __name__ == "__main__":
    main()
