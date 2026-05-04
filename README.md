# API REST con Django Rest Framework

Este proyecto implementa una API REST con Django Rest Framework para gestionar usuarios y tareas.

## Tecnologías utilizadas

- Python
- Django
- Django Rest Framework

### User
Se utiliza el modelo de usuario incorporado por Django.

Campos utilizados:
- id
- username
- email

### Task
Modelo creado para gestionar tareas.

Campos:
- id
- title
- description
- completed
- user

#### GET /api/users/
Devuelve la lista de usuarios.

#### POST /api/users/
Crea un nuevo usuario.

#### GET /api/users/<id>/
Devuelve un usuario específico.

#### PUT /api/users/<id>/
Actualiza un usuario específico.

#### DELETE /api/users/<id>/
Elimina un usuario específico.

#### GET /api/tasks/
Devuelve la lista de tareas.

#### POST /api/tasks/
Crea una nueva tarea.

#### GET /api/tasks/<id>/
Devuelve una tarea específica.

#### PUT /api/tasks/<id>/
Actualiza una tarea específica.

#### DELETE /api/tasks/<id>/
Elimina una tarea específica.

## Ejemplo de tarea

```json
{
    "title": "Estudiar DRF",
    "description": "Crear la API del ejercicio",
    "completed": false,
    "user": 1
}