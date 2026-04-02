from fastapi import FastAPI
from fastapi.security import HTTPBearer
from src.interfaces.api.routes import auth_routes, docente_routes
from src.infrastructure.db.connection import engine
from src.infrastructure.db.models import Base

app = FastAPI(
    title="Usuarios Docentes Service",
    description="Microservicio para gestión de docentes en sistema educativo",
    version="1.0.0",
)

security = HTTPBearer()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(docente_routes.router)