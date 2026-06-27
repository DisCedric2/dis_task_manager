# Django Task Manager API

A RESTful Task Management API built using Django REST Framework with JWT Authentication and Role-Based Access Control (RBAC).

## Features

* User Registration
* JWT Authentication
* Refresh Token Support
* Role-Based Access Control (Admin/User)
* CRUD Operations for Tasks
* Pagination
* Filtering
* Search Functionality
* SQLite Database

---

## Technology Stack

* Python 3.9+
* Django 5+
* Django REST Framework
* SimpleJWT
* SQLite
* Django Filter

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd dis-task-manager-api
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

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

Start server:

```bash
python manage.py runserver
```

---

## Role Assignment

The project uses Django's built-in Groups for Role-Based Access Control.

Available Roles:

- Admin
- User

To assign a role:

1. Login to Django Admin:
   http://127.0.0.1:8000/admin/

2. Navigate to:
   Authentication and Authorization → Groups

3. Create groups:
   - Admin
   - User

4. Navigate to:
   Authentication and Authorization → Users

5. Open a user and assign the desired group.

## Authentication Endpoints

### Register

```http
POST /api/auth/register/
```

Example:

```json
{
    "username":"user1",
    "email":"user1@gmail.com",
    "password":"password123"
}
```

---

### Login

```http
POST /api/auth/login/
```

Example:

```json
{
    "username":"user1",
    "password":"password123"
}
```

Returns:

```json
{
    "refresh":"...",
    "access":"..."
}
```

---

### Refresh Token

```http
POST /api/auth/refresh/
```

---

## Task Endpoints

| Method | Endpoint         |
| ------ | ---------------- |
| GET    | /api/tasks/      |
| POST   | /api/tasks/      |
| GET    | /api/tasks/<id>/ |
| PATCH  | /api/tasks/<id>/ |
| DELETE | /api/tasks/<id>/ |

---

## Role Based Access

### Admin

* View all tasks
* Create tasks
* Update any task
* Delete any task

### User

* View only own tasks
* Create own tasks
* Update own tasks
* Delete own tasks

---

## Bonus Features

* Pagination
* Search
* Filter by status
* Due date support
* Ordering support

---

## Authorization Header

```http
Authorization: Bearer <access_token>
```
