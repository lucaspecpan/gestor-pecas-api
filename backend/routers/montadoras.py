from fastapi import APIRouter, HTTPException, status
from backend.database import conn

router = APIRouter(prefix="/montadoras", tags=["Montadoras"])

@router.get("/")
def listar_montadoras():
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, nome, codigo FROM montadoras ORDER BY nome")
        rows = cur.fetchall()
        cur.close()
        return [{"id": r[0], "nome": r[1], "codigo": r[2]} for r in rows]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/")
def criar_montadora(payload: dict):
    nome = payload.get("nome")
    if not nome:
        raise HTTPException(status_code=400, detail="Nome é obrigatório.")

    try:
        cur = conn.cursor()
        # Verifica duplicidade
        cur.execute("SELECT 1 FROM montadoras WHERE nome = %s", (nome,))
        if cur.fetchone():
            raise HTTPException(status_code=400, detail="Montadora já existe.")

        # Busca próximo código
        cur.execute("SELECT valor_atual FROM montadora_codigo_seq WHERE id = 1")
        atual = cur.fetchone()
        if not atual:
            raise HTTPException(status_code=500, detail="Sequência de código não encontrada.")

        novo_codigo = atual[0] + 1

        # Atualiza sequência
        cur.execute("UPDATE montadora_codigo_seq SET valor_atual = %s WHERE id = 1", (novo_codigo,))

        # Insere nova montadora
        cur.execute(
            "INSERT INTO montadoras (nome, codigo) VALUES (%s, %s) RETURNING id",
            (nome, novo_codigo)
        )
        nova_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return {"id": nova_id, "nome": nome, "codigo": novo_codigo}

    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
