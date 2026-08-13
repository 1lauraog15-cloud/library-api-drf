# library-api-drf

Proyecto de práctica con **Django** y **Django REST Framework**. Contiene dos aplicaciones:

- **`books`**: aplicación Django clásica con un modelo `Book` y una vista de listado renderizada con plantillas.
- **`api`**: API REST construida con Django REST Framework para gestionar usuarios (modelo `User` de Django) y tareas (modelo `Task`).

La base de datos por defecto es SQLite, pensada para ejecución local.

## Tecnologías

- Python 3.11
- Django 5.1
- Django REST Framework
- SQLite

## Instalación

```bash
git clone https://github.com/1lauraog15-cloud/library-api-drf.git
cd library-api-drf

# Con pipenv (el proyecto incluye Pipfile)
pipenv install
pipenv shell

# Alternativa con venv + pip
python -m venv .venv
source .venv/bin/activate        # en Windows: .venv\Scripts\activate
pip install django djangorestframework
```

## Variables de entorno

Copia `.env.example` a `.env` y ajusta los valores. El fichero `.env` está incluido en `.gitignore` y no debe subirse nunca al repositorio.

| Variable | Obligatoria | Por defecto | Descripción |
| --- | --- | --- | --- |
| `DJANGO_SECRET_KEY` | Sí en producción | clave de desarrollo insegura | Clave de firma criptográfica de Django. Generar una propia con `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`. |
| `DJANGO_DEBUG` | No | `True` | Modo debug. Debe ser `False` en producción. |
| `DJANGO_ALLOWED_HOSTS` | Sí si `DJANGO_DEBUG=False` | vacío | Lista de hosts permitidos separados por comas. |

Las variables se leen del entorno del proceso. Por ejemplo:

```bash
export DJANGO_SECRET_KEY="tu-clave-generada"
export DJANGO_DEBUG=False
export DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
```

## Ejecución

```bash
python manage.py migrate
python manage.py createsuperuser   # opcional, para acceder al admin
python manage.py runserver
```

El servidor queda disponible en `http://127.0.0.1:8000/`.

- `/` — listado de libros (app `books`)
- `/admin/` — panel de administración de Django
- `/api/` — endpoints de la API REST

## Modelos

### User
Se utiliza el modelo de usuario incorporado por Django.

Campos expuestos por la API:
- `id`
- `username`
- `email`

### Task
Modelo creado para gestionar tareas.

Campos:
- `id`
- `title`
- `description`
- `completed`
- `user` (clave foránea a `User`)

### Book
Modelo de la app `books`.

Campos:
- `id`
- `title`
- `subtitle`
- `author`
- `isbn`

## Endpoints de la API

| Método | Ruta | Descripción |
| --- | --- | --- |
| GET | `/api/users/` | Devuelve la lista de usuarios. |
| POST | `/api/users/` | Crea un nuevo usuario. |
| GET | `/api/users/<id>/` | Devuelve un usuario específico. |
| PUT | `/api/users/<id>/` | Actualiza un usuario específico. |
| DELETE | `/api/users/<id>/` | Elimina un usuario específico. |
| GET | `/api/tasks/` | Devuelve la lista de tareas. |
| POST | `/api/tasks/` | Crea una nueva tarea. |
| GET | `/api/tasks/<id>/` | Devuelve una tarea específica. |
| PUT | `/api/tasks/<id>/` | Actualiza una tarea específica. |
| DELETE | `/api/tasks/<id>/` | Elimina una tarea específica. |

## Ejemplo de tarea

```json
{
    "title": "Estudiar DRF",
    "description": "Crear la API del ejercicio",
    "completed": false,
    "user": 1
}
```

## Estructura del proyecto

```
library-api-drf/
├── api/                  # App de la API REST (modelo Task, serializers, vistas, urls)
├── books/                # App de libros (modelo Book, vista de listado, plantilla)
├── library_project/      # Configuración del proyecto Django (settings, urls, wsgi, asgi)
├── manage.py
├── Pipfile / Pipfile.lock
└── .env.example          # Plantilla de variables de entorno
```

## Nota sobre seguridad

Este repositorio contuvo inicialmente la `SECRET_KEY` de desarrollo generada automáticamente por `django-admin startproject` (prefijo `django-insecure-`). La configuración actual lee la clave desde la variable de entorno `DJANGO_SECRET_KEY`. Genera siempre una clave nueva para cualquier despliegue real.
