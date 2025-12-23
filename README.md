# 📝 Blog Application Design

A robust and secure multi-user blog application built with **Django**. This project demonstrates a full-stack implementation featuring user authentication, CRUD operations, permission management, and a responsive UI using Bootstrap 5.

---

## 📑 Table of Contents

- [📝 Blog Application Design](#-blog-application-design)
  - [📑 Table of Contents](#-table-of-contents)
  - [✨ Features](#-features)
  - [🛠 Tech Stack](#-tech-stack)
  - [📋 Prerequisites](#-prerequisites)
  - [🚀 Installation \& Setup](#-installation--setup)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create and Activate a Virtual Environment](#2-create-and-activate-a-virtual-environment)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Database Setup](#4-database-setup)
    - [5. Run the Server](#5-run-the-server)
  - [📖 Usage Guide](#-usage-guide)
  - [📂 Project Structure](#-project-structure)
  - [📸 Screenshots](#-screenshots)
    - [Home Page](#home-page)
    - [Login Interface](#login-interface)

---

## ✨ Features

*   **🔐 User Authentication**: Secure registration, login, and logout functionality.
*   **📝 Blog Management**: Create, read, update, and delete (CRUD) blog posts.
*   **🛡️ Permission Control**: Object-level permissions ensure users can only edit or delete their own posts.
*   **🎨 Responsive Design**: Clean and modern interface styled with **Bootstrap 5**.
*   **🖼️ Media Support**: Support for uploading header images for blog posts.
*   **⚙️ Admin Interface**: Comprehensive dashboard for administrators to manage users and content.

---

## 🛠 Tech Stack

*   **Backend**: Python, Django
*   **Frontend**: HTML5, CSS3, Bootstrap 5
*   **Database**: SQLite (Default)
*   **Version Control**: Git

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
*   [Python 3.x](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/downloads)

---

## 🚀 Installation & Setup

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/ruihaoGitHub/Blog_Application_Design.git
cd Blog
```

### 2. Create and Activate a Virtual Environment

It is best practice to run Django projects in a virtual environment.

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Apply migrations to set up the database schema.

```bash
python manage.py migrate
```

*(Optional)* Create a superuser to access the Django Admin panel:

```bash
python manage.py createsuperuser
```

### 5. Run the Server

Start the local development server:

```bash
python manage.py runserver
```

Open your browser and navigate to: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📖 Usage Guide

1.  **Sign Up**: Click on the "Sign up" link in the navigation bar to create a new account.
2.  **Log In**: Access your account using your credentials.
3.  **Create Post**: Click "Add new post" to write a blog entry.
4.  **Edit Post**: Click "Edit" on any post you own to modify it.
5.  **Admin Panel**: Go to `/admin/` and log in with your superuser account to manage all users and posts.

---

## 📂 Project Structure

```
Blog/
├── Blog/                   # Project configuration
│   ├── settings.py         # Main settings file
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py             # WSGI application entry point
├── blogs/                  # Main application app
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JS, Images)
│   ├── templates/          # HTML templates
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   └── urls.py             # App-specific URLs
├── media/                  # User-uploaded content
├── templates/              # Global templates (e.g., login)
├── db.sqlite3              # SQLite database
├── manage.py               # Django command-line utility
└── requirements.txt        # Project dependencies
```

---

## 📸 Screenshots

### Home Page
![Home Page](images/home_page.png)
*Overview of recent blog posts.*

### Login Interface
![Login Page](images/login_page.png)
*Secure user login page.*
