from fastapi import APIRouter, HTTPException
from auth.auth_service import authenticate_user
from auth.auth_utils import create_access_token

router = APIRouter()

@router.post("/login")
def login(data: dict):
    user = authenticate_user(data["username"], data["password"])

    if not user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token({"sub": user["username"]})

    return {"access_token": token, "token_type": "bearer"}
