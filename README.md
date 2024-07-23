# TalkBag

This project is a full-stack web application built with Django, focused on robust user authentication, security, and seamless user registration. It allows authenticated users to securely create, edit, delete, and search talks (messages) with optional photo uploads. The application ensures efficient management of user-generated content while prioritizing user privacy and data security.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Features

Describe the main features of your project, including functionalities such as:
- User registration and authentication
- Creating, editing, deleting talks (messages)
- Uploading and displaying photos with talks
- Searching talks
- etc.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/gagan9214/TalkBag.git
   cd your_project

Create a virtual environment:
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:
- pip install -r requirements.txt

Apply database migrations:
- python manage.py migrate

Create a superuser:
- python manage.py createsuperuser

Run the development server:
- python manage.py runserver

Access the application at http://localhost:8000.

## Usage

Register a new user:
- Navigate to /register/ and fill out the registration form.

Login:
- Navigate to /login/ to login with your registered credentials.

Create a new talk:
- Once logged in, navigate to /create/ to create a new talk. You can upload a photo along with your talk.

Edit or delete talks:
- Each talk you create will have options to edit or delete it.

Search talks:
- Use the search functionality / to find talks containing specific keywords.

## Technologies Used
- Django
- HTML/CSS
- Bootstrap
- SQLite (default database used by Django)

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.
