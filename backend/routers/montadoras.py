from fastapi import APIRouter, HTTPException
from backend.database import SUPABASE_URL, HEADERS
import requests
import json

router = APIRouter(prefix="/montadoras", tags=["Montadoras"])

@router.get("/")
def listar_montadoras():
    try:
        res = requests.get(f"{SUPABASE_URL}/rest/v1/montadoras?select=id,nome,codigo", headers=HEADERS)
        return res.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/")
def criar_montadora(data: dict):
    try:
        res = requests.post(f"{SUPABASE_URL}/rest/v1/montadoras", headers=HEADERS, data=json.dumps([data]))
        if res.status_code != 201:
            raise HTTPException(status_code=400, detail=res.text)
        return res.json()[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
