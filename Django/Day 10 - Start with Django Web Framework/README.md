# Context

- [Context](#context)
  - [Start with Django](#start-with-django)
  - [What is Django?](#what-is-django)
  - [Why use Django?](#why-use-django)
  - [Key Features of Django](#key-features-of-django)
  - [History of Django](#history-of-django)
  - [The MVT Architecture](#the-mvt-architecture)
  - [Setup First Django Project](#setup-first-django-project)

## Start with Django

## What is Django?

- Django is a high-level Python web framework
- It helps developers build secure and scalable web applications
- Comes with many built-in features

---
[⬆️ Go to Context](#context)

## Why use Django?

- Fast development
- Built-in admin panel
- Secure - Protection against common attacks ( SQL injection, CSRF Protection,  Cross-Site Scripting (XSS Protection), etc.)
- Scalable for large applications
- Clean and readable code structure

---
[⬆️ Go to Context](#context)

## Key Features of Django

- ORM (Object Relational Mapper)
- Built-in authentication system
- URL routing system
- Admin dashboard
- Form handling
- Middleware support

---
[⬆️ Go to Context](#context)

## History of Django

- Django was invented by Lawrence Journal-World in 2003
- Initial release to the public was in July 2005
- Latest version of Django is 6.0.4 (April 7, 2026)

---
[⬆️ Go to Context](#context)

## The MVT Architecture

> Django follows the MVT (Model-View-Template) architectural pattern, which is a variation of the traditional MVC (Model-View-Controller) design pattern used in web development. This pattern separates the application into three main components:

| Concept    | MVC                  | Django (MVT)                |
| ---------- | -------------------- | --------------------------- |
| Model      | Handles data & logic | Handles data & logic        |
| View       | UI layer             | **Template (HTML)**         |
| Controller | Handles user input   | **View (Python functions)** |
| Framework  | Passive              | **Active controller**       |

![Django Request Response Cycle](https://i.imgur.com/WvqUs8P.gif)

- Model (same as MVC): Manages the data — built using Django’s ORM. Defines the structure of your database.
- View (different from MVC): In Django, the “View” contains the business logic. It fetches data from the model and passes it to the template.
- Template: Responsible for rendering the final HTML — your front-end content.

---
[⬆️ Go to Context](#context)

## Setup First Django Project

- Create virtual environment

  ```sh
  py -m venv .venv
  ```

- Activate `.venv`

  ```sh
  .venv\Scripts\activate
  ```

- Install [Django](https://pypi.org/project/Django/)

  ```sh
  pip install Django
  ```

- Create first project (passing `.` to create the project in the current directory)

  ```sh
  django-admin startproject firstProject .
  ```

- Run the server

  ```sh
  py manage.py runserver
  ```

  - now open http://127.0.0.1:8000/ in the browser

---
[⬆️ Go to Context](#context)
