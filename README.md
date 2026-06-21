# 📚 Library Management System – Django REST Framework (Final Project)

## 🚀 Overview

This project is a full backend REST API system built with **Django REST Framework**.  
It simulates a **Library Management System** with authentication, caching, background tasks, and Dockerized deployment.

---

## ⚙️ Tech Stack

- Python 3.12+
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Flower
- Docker & Docker Compose
- Simple JWT Authentication
- Swagger (drf-yasg)

---

## 📦 Features

### 🔐 Authentication
- User Registration
- Login (JWT)
- Refresh Token
- Protected endpoints

### 📚 Library System
- Books CRUD (Create, Read, Update, Delete)
- Borrow system (users borrow books)
- Relationships between models (ForeignKey, ManyToMany, OneToOne)

### ⚡ Performance
- Redis caching for list endpoints
- Cache timeout configured
- Unique cache keys

### 🔄 Background Tasks (Celery)
- Send welcome email after registration
- Background task execution via Redis broker

### 📧 Email System
- Email sent automatically after user registration using Celery worker

### 📊 API Documentation
- Swagger UI available
- Redoc documentation available
- All endpoints tested via Swagger

### 🧪 Testing
- Model tests
- API tests
- Authentication tests

---

## 🧱 Project Structure
final_work/
│
├── backend/
│ ├── books/
│ ├── users/
│ ├── borrow/
│ ├── library_project/
│ ├── manage.py
│ ├── Dockerfile
│ ├── requirements.txt
│
├── docker-compose.yml
├── .env
├── .gitignore
├── README.md


---

## 🚀 How to Run the Project

### 1. Clone Repository

git clone https://github.com/YOUR_USERNAME/final_work.git
cd final_work
2. Build and Start Containers
docker-compose up --build
3. Run Migrations
docker-compose exec web python manage.py migrate
4. Create Superuser (optional)
docker-compose exec web python manage.py createsuperuser
🌐 Services URLs
Service	URL
Django API	http://localhost:8000
Swagger UI	http://localhost:8000/swagger/
Redoc UI	http://localhost:8000/redoc/
Flower (Celery Monitor)	http://localhost:5555
🔐 API Endpoints
Authentication
POST /api/register/
POST /api/login/
POST /api/token/refresh/
Books API
GET    /api/books/
POST   /api/books/
GET    /api/books/{id}/
PUT    /api/books/{id}/
DELETE /api/books/{id}/
Borrow System
POST /api/borrow/
GET  /api/borrow/
⚡ Celery Tasks
Send welcome email after registration
Background task processing using Redis broker
Worker runs independently in Docker
📊 Redis Cache
Book list endpoint is cached
Improves performance
Cache timeout configured
Unique cache keys used
🐳 Docker Services

This project runs using Docker Compose:

web (Django)
db (PostgreSQL)
redis
celery worker
flower
🧪 Running Tests

Run all tests inside Docker:

docker-compose exec web python manage.py test
📌 Important Notes
Use .env file for environment variables
Never upload secrets to GitHub
Redis is required for Celery + caching
All services start with one command: docker-compose up
📷 Required Submission Checklist

Make sure you include:

✔ GitHub repository
✔ docker-compose.yml
✔ Swagger URL screenshots
✔ Postman or Swagger testing screenshots
✔ Flower working screenshot
✔ Celery worker logs screenshot
✔ Docker containers screenshot
✔ README file (this file)

🚀 Start Project
docker-compose up --build
👩‍💻 Author

Final Project – Django REST Framework API
Student: Mariam
