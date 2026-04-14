# Context

- [Context](#context)
  - [Create Django project](#create-django-project)
  - [Create Superuser](#create-superuser)
  - [HttpResponse](#httpresponse)

## Create Django project

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

## Create Superuser

- To Create Superuser in new project first we need to migrate it

  ```sh
  py manage.py migrate
  ```

  ```sh
  py manage.py createsuperuser
  ```

  - Setup username and password
  - Now go to http://127.0.0.1:8000/admin and enter that username and password to login

---
[⬆️ Go to Context](#context)

## HttpResponse

- Simple *"Hello World"* text show using `HttpResponse`
  - Create [firstProject/views.py](./firstProject/views.py) file inside project directory

    ```py
    from django.http import HttpResponse

    def home_page(request):
      msg="Hello World"
      return HttpResponse(msg)
    ```

  - Now add this function in the [firstProject/urls.py](./firstProject/urls.py) file path list

    ```py
    from django.contrib import admin
    from django.urls import path
    from . import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',views.home_page,name='home')
    ]
    ```

  - Now visit http://127.0.0.1:8000/ to see the output

---
[⬆️ Go to Context](#context)
