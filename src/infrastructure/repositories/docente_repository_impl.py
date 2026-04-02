from src.application.ports.docente_repository import DocenteRepository
from src.infrastructure.db.models import DocenteModel
from src.infrastructure.db.connection import SessionLocal

class DocenteRepositoryImpl(DocenteRepository):

    def save(self, data):
        with SessionLocal() as db:
            docente = DocenteModel(**data)
            db.add(docente)
            db.commit()
            db.refresh(docente)
            return docente

    def find_by_email(self, correo):
        with SessionLocal() as db:
            return db.query(DocenteModel).filter_by(correo=correo).first()

    def get_all(self):
        with SessionLocal() as db:
            return db.query(DocenteModel).all()