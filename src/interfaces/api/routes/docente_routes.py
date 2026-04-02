from typing import List

from fastapi import APIRouter, Depends, HTTPException, Header, status
from src.infrastructure.repositories.docente_repository_impl import DocenteRepositoryImpl
from src.application.use_cases.get_docentes import GetDocentes
from src.infrastructure.security.jwt import verify_token
from src.interfaces.api.schemas.docente_schema import DocenteResponse

router = APIRouter()
repo = DocenteRepositoryImpl()


def get_current_user(authorization: str | None = Header(None, alias="Authorization")):
    if authorization is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header missing",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization header must be Bearer token",
        )

    token = authorization.split(" ", 1)[1]
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