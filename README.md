# Student Management System

This is a beginner-friendly Django web application that allows you to **create, view, update, and delete student records**. It’s a simple CRUD project designed to practice Django basics such as models, views, forms, and templates.

---

## Features
- View a list of all students  
- Add a new student with name, age, and email  
- Update existing student details  
- Delete a student after confirmation  
- User-friendly interface with form validation  

---

## Technologies Used
- Python 3.x  
- Django 4.x  
- SQLite (default database, can be switched to MySQL)  
- HTML & CSS for templates  
- Pipenv for virtual environment management  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/muslimamaliha/maliha_ID23028.git
cd maliha_ID23028/student_project

2. Create and activate a virtual environment using Pipenv
pip install pipenv
pipenv shell

3. Install dependencies
pipenv install -r requirements.txt

4. Apply migrations
python manage.py migrate

6. Run the development server
python manage.py runserver

7. Open in browser
http://127.0.0.1:8000/

Project Structure
student_app/         — Contains model, views, and forms for Student CRUD  
templates/           — HTML templates for forms, list, and delete confirmation  
student_project/     — Django project settings and URLs  
Pipfile              — Pipenv environment file  
requirements.txt     — Project dependencies  

License
This project is open-source and free to use.
