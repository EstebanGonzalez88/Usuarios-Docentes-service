class CreateDocente:
    def __init__(self, repository, hash_service):
        self.repository = repository
        self.hash_service = hash_service

    def execute(self, data):
        if self.repository.find_by_email(data["correo"]):
            raise ValueError("El correo ya está registrado")

        data["password"] = self.hash_service(data["password"])
        data.setdefault("rol", "DOCENTE")
        data.setdefault("estado", True)
        return self.repository.save(data)