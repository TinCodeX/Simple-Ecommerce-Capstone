# E-commerce Platform API

A robust and scalable **RESTful API** for managing an e-commerce platform, built using **Django** and **Django REST Framework (DRF)**.
This API provides complete backend functionality for **product management, user authentication, wishlists, and secure access using JWT**.

The project focuses on **clean architecture, performance, and real-world backend practices**, making it suitable for **learning, portfolio use, and production-ready extensions**.

---

# Features

### Product Management

Full **CRUD operations** for products and categories.

### Product Search & Filtering

Search products by name and filter them by category.

### User Management

Custom user model with **registration and profile management endpoints**.

### Authentication & Authorization

Secure **JWT-based authentication** using **SimpleJWT**.

### Wishlist System

User-specific **wishlist functionality**.

### Database Management

Efficient data handling using the **Django ORM**.

---

# Tech Stack

Framework: **Django 6.0.2**
API Engine: **Django REST Framework (DRF)**
Authentication: **SimpleJWT**
Database: **SQLite** (default, configurable)

---

# Getting Started

## Prerequisites

* Python 3.8+
* pip

# Installation

Clone the repository

git clone <repository-url>
cd ecommerce-api

Create and activate a virtual environment

python -m venv venv

Windows

venv\Scripts\activate

Linux / macOS

source venv/bin/activate

Install dependencies


pip install -r requirements.txt


Apply migrations


cd ecommerce
python manage.py makemigrations accounts products cart orders payments
python manage.py migrate

Run the development server


python manage.py runserve

Access the API at:

http://127.0.0.1:8000/


# API Endpoints

## Products

GET `/api/products/` – List all products (supports `?search=` and `?category=`)

POST `/api/products/create/` – Create a new product (Authenticated/Admin)

GET `/api/products/<id>/` – Retrieve product details

PUT `/api/products/<id>/` – Update a product

PATCH `/api/products/<id>/` – Partially update a product

DELETE `/api/products/<id>/` – Delete a product

---

## Accounts

POST `/api/accounts/register/` – Register a new user

GET `/api/accounts/profile/` – Retrieve or update user profile

POST `/api/token/` – Obtain JWT access and refresh tokens

POST `/api/token/refresh/` – Refresh access token

---

## Wishlist

GET `/api/products/wishlist/` – Retrieve user wishlist

POST `/api/products/wishlist/` – Add product to wishlist

DELETE `/api/products/wishlist/` – Remove product from wishlist

---

# Running Tests

python manage.py test products accounts

---

# Project Goals

* Build a clean and scalable REST API
* Implement secure authentication
* Apply best practices in Django backend development
* Create a strong **portfolio-grade backend system**

---

# Future Improvements

* Order and checkout system
* Payment gateway integration (Stripe / PayPal)
* Product reviews and ratings
* Admin analytics dashboard
* Caching and performance optimization

---

# Author

**Tinsae Befekadu Guma**
Software Engineering Student | Backend & Full-Stack Developer
