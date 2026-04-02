# Usuarios Docentes Service

Microservicio `usuarios/docentes-service` para un sistema educativo basado en microservicios.

## Descripción

Este proyecto implementa un servicio de gestión de docentes con FastAPI y una arquitectura hexagonal (dominio, aplicación, infraestructura e interfaces). Permite registrar docentes, autenticarlos y listar docentes protegidos por JWT.

## Tecnologías

- Python 3.12
- FastAPI
- SQLAlchemy
- MySQL / MariaDB
- PyMySQL
- Passlib (bcrypt)
- python-jose
- Pydantic

## Estructura

- `main.py`: arranca la aplicación y crea las tablas en startup.
- `src/domain`: entidades del dominio.
- `src/application`: casos de uso y puertos.
- `src/infrastructure`: repositorios, conexión DB y seguridad.
- `src/interfaces/api`: rutas y esquemas API.

## Instalación

```bash
cd c:/Taller4/usuariosdocentes-service
python -m venv rabbit
rabbit\Scripts\activate
pip install -r requirements.txt
```

> Si usas WSL o Linux, ajusta las rutas a `/mnt/c/taller4/usuariosdocentes-service`.

## Configuración

Crea un archivo `.env` con al menos:

```env
DATABASE_URL=mysql+pymysql://root:1234@localhost/docentes_db
JWT_SECRET=tu_secreto
```

El servicio intentará crear la base de datos `docentes_db` si no existe.

## Ejecución

```bash
uvicorn main:app --reload --port 8001
```

## Endpoints principales

- `POST /auth/register`: registrar docente
- `POST /auth/login`: obtener token JWT
- `GET /docentes`: listar docentes (requiere header `Authorization: Bearer <token>`)

## Notas

- Se recomienda no versionar la carpeta `rabbit/` ni `.env`.
- Ya está inicializado el repositorio Git y subido al remoto:
  - `https://github.com/EstebanGonzalez88/Usuarios-Docentes-service`
