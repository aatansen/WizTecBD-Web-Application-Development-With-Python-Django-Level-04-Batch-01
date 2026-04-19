# Context

- [Context](#context)
  - [Django Project Setup](#django-project-setup)
  - [Django App Setup](#django-app-setup)
  - [Django Model](#django-model)
  - [Django `makemigrations` vs `migrate`](#django-makemigrations-vs-migrate)
  - [Apply New Changes To Database](#apply-new-changes-to-database)
  - [Add Data From Admin Page](#add-data-from-admin-page)
  - [Show Data In Frontend](#show-data-in-frontend)

## Django Project Setup

- First create and activate `venv`
- Install `django`
- Create a project `school_project`

- Setup Database (Initial Migration)

  ```sh
  py manage.py makemigrations
  py manage.py migrate
  ```

- Create superuser (admin user)

  ```sh
  py manage.py createsuperuser
  ```

---
[⬆️ Go to Context](#context)

## Django App Setup

- Create an app

  ```sh
  py manage.py startapp school_app
  ```

- Add this app name in [settings.py](./school_project/settings.py) within `INSTALLED_APPS`

  ```py
  INSTALLED_APPS = [
      ...
      'school_app',
  ]
  ```

---
[⬆️ Go to Context](#context)

## Django Model

![Django Model](https://i.imgur.com/LBW8872.png)
![Django MVT](https://i.imgur.com/5m8x2SJ.png)

- Django Model Concept and some keywords

  | Database Term  | Django Term       | What It Means                        | Example                      |
  | -------------- | ----------------- | ------------------------------------ | ---------------------------- |
  | Entity         | Model             | A real-world object                  | `StudentModel`               |
  | Attribute      | Field             | Property of an entity                | `name`, `age`                |
  | Table          | DB Table          | Stores all records of a model        | `student_table`              |
  | Record (Row)   | Model Instance    | One single data entry                | `StudentModel(name="TT")`    |
  | Primary Key    | `id` field        | Unique identifier for each record    | `id=1`                       |
  | Foreign Key    | `ForeignKey`      | Many-to-one relationship             | StudentModel → TeacherModel  |
  | Many-to-Many   | `ManyToManyField` | Many-to-many relationship            | StudentModel ↔ CourseModel   |
  | One-to-One     | `OneToOneField`   | One-to-one relationship              | UserModel ↔ ProfileModel     |
  | Query Language | ORM               | Python way to interact with database | `StudentModel.objects.all()` |
  | Schema Change  | Migration         | Updates DB structure                 | `makemigrations`             |
  | Validation     | `blank=True`      | Form-level optional field            | Empty allowed in form        |
  | DB Constraint  | `null=True`       | Database-level optional field        | NULL allowed in DB           |
  | Default Value  | `default=`        | Predefined value if none given       | `age=18`                     |
  | Metadata       | `Meta` class      | Model configuration                  | ordering, table name         |
  | Representation | `__str__()`       | Human-readable object name           | `"TT"`                       |

- Now we will create model in [school_app/models.py](./school_app/models.py)

  ```py
  from django.db import models

  class TeacherModel(models.Model):
      name = models.CharField(max_length=100)
      address = models.CharField(max_length=100)
      email = models.EmailField()
  ```

- Register this model in [admin.py](./school_app/admin.py)

---
[⬆️ Go to Context](#context)

## Django `makemigrations` vs `migrate`

- **makemigrations**
  - Creates migration files based on model changes
  - Does NOT touch the database
  - Scans models.py
  - Detects changes (new model, field, delete, etc.)
  - Generates a migration file inside:
  - `app_name/migrations/`

- **migrate**
  - Applies migration files to the database
  - Reads migration files
  - Executes SQL queries
  - Updates database schema

---
[⬆️ Go to Context](#context)

## Apply New Changes To Database

- To see current migration status

  ```sh
  py manage.py showmigrations
  ```

- Apply migration

  ```sh
  py manage.py makemigrations
  py manage.py migrate school_app
  ````

> [!NOTE]
>
> - Each time we create a new model
> - Each time we change anything to an existing model(modify fields)
> - We have to run both `makemigrations` and `migrate` command

---
[⬆️ Go to Context](#context)

## Add Data From Admin Page

- Login using `username` and `password` which is setup during `createsuperuser` command
- Now add data

---
[⬆️ Go to Context](#context)

## Show Data In Frontend

- Create [templates](./templates/) folder in project root directory where [manage.py](./manage.py) is
- Add template path in [settings.py](./school_project/settings.py)
  - Create files by following structure

    ```txt
    📁 templates
    ├── 📁 master
    │   ├── 🌐 base.html
    │   └── 🌐 nav.html
    ├── 🌐 home.html
    └── 🌐 teacher.html
    ```

  - Apply bootstrap
  - Create function in [views.py](./school_project/views.py)
  - Add `urlpatterns` in [urls.py](./school_project/urls.py)

- Now in teacher function which we created in [views.py](./school_project/views.py) we need to get data from the database

  ```py
  from django.shortcuts import render
  from school_app.models import TeacherModel

  def teacher_page(request):

    teacher_data=TeacherModel.objects.all()

    context={
      'teacher_data':teacher_data
    }

    return render(request,'teacher.html',context=context)
  ```

- In HTML page which is [teacher.html](./templates/teacher.html) we will use a bootstrap table where Django template `for loop` will be used to `iterate` over the data, and the values will be displayed using `{{ }}` syntax.

  ```jinja
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Email</th>
        <th scope="col">Address</th>
      </tr>
    </thead>
    <tbody>
      {% for teacher in teacher_data %}
      <tr>
        <td>{{teacher.name}}</td>
        <td>{{teacher.email}}</td>
        <td>{{teacher.address}}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
  ```

---
[⬆️ Go to Context](#context)
