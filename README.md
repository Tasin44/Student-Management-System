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

source venv/bin/activate   # On Windows: venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

Apply the database migrations:

python manage.py migrate

Create a superuser (admin account):

python manage.py createsuperuser

Run the development server:

    python manage.py runserver

🌐 Access the Application

Open your browser and navigate to:

http://127.0.0.1:8000/

📬 Key Routes (if using views)

    Login: /login/

    Password Reset: /reset-password/

    Student Dashboard: /student/dashboard/

    Teacher Dashboard: /teacher/dashboard/

    Admin Dashboard: /admin/dashboard/
