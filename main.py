from fastapi import FastAPI
from src.interfaces.api.routes import auth_routes, docente_routes
from src.infrastructure.db.connection import engine
from src.infrastructure.db.models import Base

app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(docente_routes.router)