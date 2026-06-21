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
