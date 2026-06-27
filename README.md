# Django Task Manager API

A RESTful Task Management API built using Django REST Framework featuring JWT Authentication, Role-Based Access Control (RBAC), Docker support, filtering, pagination, search, ordering, and unit tests.

---

# Features

### Authentication

* User Registration
* JWT Authentication
* Refresh Token Support

### Task Management

* Create Task
* Read Task
* Update Task
* Delete Task

### Role-Based Access Control

* Admin Role
* User Role

### Bonus Features

* Pagination
* Filtering
* Search
* Ordering
* Due Date Support

### Additional Features

* Docker Support
* Unit Tests
* SQLite Database

---

# Technology Stack

* Python 3.9+
* Django 6
* Django REST Framework
* SimpleJWT
* Django Filter
* SQLite
* Docker

---

# Project Structure

```text
dis_task_manager/
│
├── accounts/
├── dis_task/
├── task_manager/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

# Installation (Traditional Method)

Clone the repository:

```bash
git clone https://github.com/DisCedric2/dis_task_manager.git
cd dis_task_manager
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run development server:

```bash
python manage.py runserver
```

Application runs at:

```text
http://127.0.0.1:8000/
```

---

# Installation (Docker Method)

Build Docker image:

```bash
docker compose build
```

Run containers:

```bash
docker compose up
```

Or run in detached mode:

```bash
docker compose up -d
```

The application will be available at:

```text
http://localhost:8000/
```

To stop containers:

```bash
docker compose down
```

---

# Role Assignment

The project uses Django Groups for Role-Based Access Control.

Available roles:

* Admin
* User

## Steps

Open Django Admin:

```text
http://127.0.0.1:8000/admin/
```

Navigate to:

```text
Authentication and Authorization → Groups
```

Create groups:

* Admin
* User

Then navigate to:

```text
Authentication and Authorization → Users
```

Assign the required role to a user.

---

# Authentication Endpoints

## Register User

```http
POST /api/auth/register/
```

Example:

```json
{
    "username": "discedric",
    "email": "",
    "password": "123456"
}
```

---

## Login

```http
POST /api/auth/login/
```

Example:

```json
{
    "username": "cedric",
    "password": "cedric"
}
```

Response:

```json
{
    "refresh": "...",
    "access": "..."
}
```

---

## Refresh Token

```http
POST /api/auth/refresh/
```

---

# Authorization Header

Include JWT token in all authenticated requests:

```http
Authorization: Bearer <access_token>
```

Example:

```http
Authorization: Bearer eyJhbGc...
```

---

# Task Endpoints

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | /api/tasks/      |
| POST   | /api/tasks/      |
| GET    | /api/tasks/<id>/ |
| PATCH  | /api/tasks/<id>/ |
| DELETE | /api/tasks/<id>/ |

---

# Role Permissions

## Admin

* View all tasks
* Create tasks
* Update any task
* Delete any task

## User

* View only their own tasks
* Create their own tasks
* Update their own tasks
* Delete their own tasks

---

# Pagination

Default page size:

```text
5 records per page
```

Example:

```http
GET /api/tasks/?page=2
```

---

# Filtering

Filter by task status:

```http
GET /api/tasks/?status=true
```

or

```http
GET /api/tasks/?status=false
```

---

# Search

Search by title or description:

```http
GET /api/tasks/?search=meeting
```

---

# Ordering

Order tasks by:

* due_date
* created_at

Examples:

```http
GET /api/tasks/?ordering=due_date
```

```http
GET /api/tasks/?ordering=-created_at (descending)
```

---

# Due Date Support

Example task creation:

```json
{
    "title": "Submit Assessment",
    "description": "Complete Django assessment",
    "status": false,
    "due_date": "2026-06-30T18:00:00Z"
}
```

---

# Unit Tests

Run tests using:

```bash
python manage.py test
```

The project includes unit tests covering:

* User Registration
* JWT Authentication
* Task CRUD Operations
* Role-Based Access Control

---

# API Testing

The APIs were tested using:

* Postman
* Django Admin

---

# Author

**Dishant Bansod**
Backend Developer Assessment Submission
