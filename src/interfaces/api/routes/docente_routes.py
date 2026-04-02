from typing import List
import logging

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.infrastructure.repositories.docente_repository_impl import DocenteRepositoryImpl
from src.application.use_cases.get_docentes import GetDocentes
from src.infrastructure.security.jwt import verify_token
from src.interfaces.api.schemas.docente_schema import DocenteResponse

router = APIRouter()
repo = DocenteRepositoryImpl()
security = HTTPBearer()

logger = logging.getLogger(__name__)


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
    try:
        logger.info(f"Usuario {current_user} solicitando lista de docentes")

        if current_user.get("rol") == "ADMIN":
            docentes = repo.get_all()
        else:
            docente = repo.find_by_id(current_user.get("id"))
            if not docente:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Docente no encontrado")
            # Convertir a diccionario normalizado como get_all()
            docentes = [{
                "id": docente.id,
                "nombre": docente.nombre,
                "correo": docente.correo,
                "rol": docente.rol or "DOCENTE",
                "estado": docente.estado if docente.estado is not None else True
            }]

        logger.info(f"Docentes encontrados: {len(docentes)}")
        return docentes
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en get_docentes: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno: {str(e)}",
        )