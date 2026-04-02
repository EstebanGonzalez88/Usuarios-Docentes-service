from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.infrastructure.repositories.docente_repository_impl import DocenteRepositoryImpl
from src.application.use_cases.get_docentes import GetDocentes
from src.infrastructure.security.jwt import verify_token
from src.interfaces.api.schemas.docente_schema import DocenteResponse

router = APIRouter()
repo = DocenteRepositoryImpl()
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
        )
    return payload


@router.get("/docentes", response_model=List[DocenteResponse])
def get_docentes(current_user: dict = Depends(get_current_user)):
    use_case = GetDocentes(repo)
    return use_case.execute()