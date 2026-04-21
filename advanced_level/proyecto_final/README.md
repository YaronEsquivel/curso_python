# Orders API - Arquitectura Hexagonal

Este proyecto implementa un servicio de gestión de órdenes utilizando FastAPI con una arquitectura hexagonal (puertos y adaptadores), aplicando buenas prácticas de seguridad, testing y calidad de código.

## Arquitectura

El proyecto sigue arquitectura hexagonal separando responsabilidades en:

- **Domain**: lógica de negocio pura (entidades y value objects)
- **Application**: casos de uso y servicios
- **Infrastructure**: acceso a base de datos, routers, mappers

### Estructura:

src/
 ├── app/
 │   ├── domain/
 │   │   ├── entities
 │   │   └── value_objects
 │   ├── application/
 │   │   └── services
 │   ├── infrastructure/
 │   │   ├── routers
 │   │   ├── repositories
 │   │   └── models
 │   │ main.py
 ├── test/

 ## Ejecución

### Con Poetry

```bash
poetry install
poetry run python -m app


---

## 4. 🔐 Seguridad

```md
## Seguridad

- Autenticación con JWT usando `python-jose`
- Dependencias seguras validadas con `pip-audit`
- Gestión de configuración con `pydantic-settings`
- Principio de menor privilegio en Docker (usuario no root)

### Auditoría de dependencias

Se ejecutó:

```bash
poetry export -f requirements.txt --without-hashes | pip-audit -r /dev/stdin


---

## 5. 🧪 Testing

```md
## Testing

Se implementaron:

- Tests unitarios (value objects y dominio)
- Tests de integración (servicios + repositorios)
- Tests E2E (FastAPI con TestClient)

### Ejecutar tests

```bash
poetry run pytest --cov=app --cov-report=html
pytest --cov=app --cov-report=html

## 6. 🐳 Docker y CI/CD

```md
## Docker

El proyecto está containerizado con Docker usando buenas prácticas:

- Imagen base ligera (`python:3.12-slim`)
- Usuario no root
- Permisos mínimos
- Read-only filesystem en runtime

### Build

```bash
docker build -t orders-api .
docker run --read-only --cap-drop ALL -p 8000:8000 orders-api


---

## 🧠 7. Diagrama

```md
## Diagrama

Cliente → FastAPI Router → Service → Domain → Repository → DB
