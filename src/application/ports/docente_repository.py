from abc import ABC, abstractmethod

class DocenteRepository(ABC):

    @abstractmethod
    def save(self, docente):
        pass

    @abstractmethod
    def find_by_email(self, correo):
        pass

    @abstractmethod
    def get_all(self):
        pass