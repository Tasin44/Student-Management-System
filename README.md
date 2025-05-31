# 🎓 Django Student Management System

A role-based student management platform built with Django. It features a custom user model, email-based login, secure password reset, parent-student linkage, notification system, and clean URL design using slugs.

## 🔐 Authentication & User Management (`authenticationapp`)

- Custom `User` model inheriting from `AbstractUser`
- Role flags: `is_student`, `is_teacher`, `is_admin`
- Email-based login with optional 6-digit login token
- Secure password reset using one-time tokens via email
- Optimized login query with indexed email field

## 📧 Password Reset

- Stores password reset tokens with timestamp
- Automatically invalidates expired tokens (1-hour expiry)
- Email-based reset link delivery

## 🏫 School App (`schoolapp`)

- Notification model linked to users
- Dashboards show unread notifications
- Mark notifications as read / clear all notifications

## 🎓 Student App (`studentapp`)

- Students linked to one parent (`OneToOneField`)
- Add, edit, delete, and view student profiles
- Slugified URLs for SEO-friendly routing
- Gender field with predefined choices
- `__str__()` for better admin readability

## ⚙️ Tech Stack

- **Backend:** Django
- **Database:** SQLite (switchable to PostgreSQL/MySQL)
- **Authentication:** Custom user model with token-based password reset

## 🧪 Testing

- Basic unit tests included for models and views
- Easily extendable test suite using `django.test`

## 🚀 Getting Started

1. Clone the repository
2. Create a virtual environment and activate it
3. Run migrations:
   ```bash
   python manage.py migrate

## 🚀 Setup Instructions to Run

Follow these steps to set up and run the project on your local machine.
✅ Prerequisites (Install First)
```bash
    Python 3.x
```
```bash

    Django 3.x or newer
```
```bash
    A SQL database (e.g., SQLite, PostgreSQL, or MySQL)
```
```bash
    Git
```
🧾 Run Locally

    Clone the repository:
```bash
git clone https://github.com/YourUsername/Student-Management-System.git
```
```bash
cd Student-Management-System
```

Create and activate a virtual environment:

```bash
python -m venv venv
```
```bash
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Apply the database migrations:
```bash
python manage.py migrate
```
Create a superuser (admin account):
```bash
python manage.py createsuperuser
```
Run the development server:
```bash
    python manage.py runserver
```
🌐 Access the Application

Open your browser and navigate to:
```bash
http://127.0.0.1:8000/
```
📬 Key Routes
🔐 Authentication (authenticationapp)

    POST /signup/ — Register a new user (student, teacher, or admin)

    POST /login/ — Login using email and password

    POST /forgot-password/ — Request password reset token via email

    POST /reset-password/<token>/ — Reset password using token

    GET /logout/ — Logout user

🏫 School Dashboard & Notifications (schoolapp)

    GET /dashboard/ — User dashboard (role-based: student/teacher/admin)

    POST /notification/mark-as-read/ — Mark all notifications as read

    POST /notification/clear-all/ — Clear all notifications

🎓 Student Management (studentapp)

    GET / — List all students

    GET /add/ — Add a new student

    GET /students/<slug>/ — View a student profile

    GET /edit/<slug>/ — Edit student information

    GET /delete/<slug>/ — Delete a student


