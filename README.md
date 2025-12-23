# Blog Application

A Django-based blog application where users can register, log in, and manage their own blog posts.

## Features

*   **User Authentication**: Secure login and registration system.
*   **Blog Management**: Create, edit, and view blog posts.
*   **Permission Control**: Users can only edit their own posts.
*   **Responsive Design**: Styled with Bootstrap 5 for a modern look.
*   **Admin Interface**: Full administrative control via Django Admin.

## Prerequisites

*   Python 3.x installed
*   Git installed

## Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/Blog.git
cd Blog
```

### 2. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

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

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Database Setup

Initialize the database:

```bash
python manage.py migrate
```

(Optional) Create a superuser to access the admin panel:

```bash
python manage.py createsuperuser
```

### 5. Run the Server

Start the development server:

```bash
python manage.py runserver
```

Open your browser and visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1.  **Sign Up**: Create a new account via the "Sign up" link.
2.  **Log In**: Log in with your credentials.
3.  **Create Post**: Click "Add new post" to write a blog entry.
4.  **Edit Post**: Click "Edit" on any post you own to modify it.
5.  **Admin Panel**: Visit `/admin/` and log in with your superuser account to manage all data.

## Screenshots

![Home Page](images/home_page.png)
*Home Page with Post List*

![Login Page](images/login_page.png)
*User Login Interface*
