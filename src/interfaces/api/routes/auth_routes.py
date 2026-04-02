import os

from fastapi import APIRouter, Header, HTTPException, status
from src.infrastructure.repositories.docente_repository_impl import DocenteRepositoryImpl
from src.application.use_cases.create_docente import CreateDocente
from src.application.use_cases.login_docente import LoginDocente
from src.infrastructure.security.hash import hash, verify
from src.infrastructure.security.jwt import create_token
from src.interfaces.api.schemas.docente_schema import DocenteCreate, DocenteLogin, DocenteResponse, TokenResponse

router = APIRouter()
repo = DocenteRepositoryImpl()

@router.post("/register", response_model=DocenteResponse, status_code=status.HTTP_201_CREATED)
def register(data: DocenteCreate):
    if data.role.upper() == "ADMIN":
        admin_key = os.getenv("ADMIN_CREATION_KEY", "secret_admin")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Para crear administradores usa /auth/register-admin con la clave adecuada",
        )

    use_case = CreateDocente(repo, hash)
    try:
        return use_case.execute(data.dict())
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))


@router.post("/register-admin", response_model=DocenteResponse, status_code=status.HTTP_201_CREATED)
def register_admin(data: DocenteCreate, x_admin_key: str = Header(None, alias="X-Admin-Key")):
    admin_key = os.getenv("ADMIN_CREATION_KEY", "secret_admin")
    if x_admin_key != admin_key:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin key inválida")

    data.role = "ADMIN"
    use_case = CreateDocente(repo, hash)
    try:
        return use_case.execute(data.dict())
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))

@router.post("/login", response_model=TokenResponse)
def login(data: DocenteLogin):
    use_case = LoginDocente(repo, verify, create_token)
    try:
        token = use_case.execute(data.correo, data.password)
        return {"token": token}
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc))