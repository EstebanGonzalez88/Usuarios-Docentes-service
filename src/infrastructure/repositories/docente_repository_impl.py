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

    def find_by_id(self, docente_id):
        with SessionLocal() as db:
            return db.query(DocenteModel).filter_by(id=docente_id).first()

    def get_all(self):
        with SessionLocal() as db:
            docentes = db.query(DocenteModel).all()
            # Serializar a dict mientras estamos en la sesión para mantener valores normalizados
            result = []
            for docente in docentes:
                result.append({
                    "id": docente.id,
                    "nombre": docente.nombre,
                    "correo": docente.correo,
                    "rol": docente.rol or "DOCENTE",
                    "estado": docente.estado if docente.estado is not None else True
                })
            return result