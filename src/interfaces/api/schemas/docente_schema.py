from pydantic import BaseModel

class DocenteCreate(BaseModel):
    nombre: str
    correo: str
    password: str
    role: str = "DOCENTE"


class DocenteLogin(BaseModel):
    correo: str
    password: str


class DocenteResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str
    estado: bool

    model_config = {
        "from_attributes": True,
    }


class TokenResponse(BaseModel):
    token: str

class DocenteLogin(BaseModel):
    correo: str
    password: str


class DocenteResponse(BaseModel):
    id: int
    nombre: str
    correo: str
    rol: str
    estado: bool

    model_config = {
        "from_attributes": True,
    }


class TokenResponse(BaseModel):
    token: str