# Context

- [Context](#context)
  - [Project Setup](#project-setup)
  - [Setup Everything Inside App](#setup-everything-inside-app)
    - [App Setup](#app-setup)
    - [Templates and Url Setup](#templates-and-url-setup)
  - [Data Add From Frontend And Show](#data-add-from-frontend-and-show)

## Project Setup

- Create `venv`
- Install Django
- Create Project `school_project`
- Initialize database
- Create Superuser

---
[⬆️ Go to Context](#context)

## Setup Everything Inside App

### App Setup

- Create App `school_app`
- Add app name inside `settings.py` file `INSTALLED_APPS` list
- Create `studentModel` model inside [models.py](./school_app/models.py)
- Register model inside [admin.py](./school_app/admin.py)
- Run database migration commands using app name

---
[⬆️ Go to Context](#context)

### Templates and Url Setup

- Create [templates](./school_app/templates/) folder inside [app directory](./school_app/)
- To show `studentModel` data we will create an HTML page [student-list.html](./school_app/templates/student-list.html)

  ```txt
  📁 templates
  ├── 📁 master
  │   ├── 🌐 base.html
  │   └── 🌐 nav.html
  └── 🌐 student-list.html
  ```

- Setup Django template inheritance
  - Setup [bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
  - Make parent-child relation between each HTML pages

- Create a function to render [student-list.html](./school_app/templates/student-list.html) inside App's [views.py](./school_app/views.py)
- Now we have to create [urls.py](./school_app/urls.py) inside App directory

  ```py
  from django.urls import path
  from school_app.views import student_list

  urlpatterns = [
      path('',student_list,name='student_list')
  ]
  ```

- We have to include this App's [urls.py](./school_app/urls.py) inside project's [urls.py](./school_project/urls.py)

  ```py
  from django.contrib import admin
  from django.urls import path,include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('',include('school_app.urls')),
  ]
  ```

- To test if everything working fine we will add data from our admin page

> [!IMPORTANT]
>
> - The directory must be named exactly `templates` inside the app directory; otherwise Django will not detect it. Previously, when creating a `templates` folder at the project level, we had to manually add its path in `TEMPLATES['DIRS']`. However, for app-level `templates` directories, no configuration is needed in `settings.py` because Django automatically discovers them when `APP_DIRS=True`.
> - When we define views at the project level, we directly add their paths in the project's `urls.py`. However, when working inside an app, we create a separate `urls.py` within that app and define routes there. Then, we include the app’s `urls.py` inside the project-level `urls.py` using `include()`.

---
[⬆️ Go to Context](#context)

## Data Add From Frontend And Show

- Now to add data from frontend we will create a new HTML page [add-student.html](./school_app/templates/add-student.html)
  - Get a bootstrap form
  - Add `method="POST"` inside form tag
  - Include `{% csrf_token %}` after form tag
  - Use same `name attribute` from the created [model.py](./school_app/models.py) field

- Create a function to render it in [views.py](./school_app/views.py)
  - We will get values from the form using `name` attribute
  - After getting data we will save this data in our model using `studentModel.objects.create()`
  - Then we will redirect user to [student-list.html](./school_app/templates/student-list.html) page using `redirect` and `url path name`

- Add this inside [urls.py](./school_app/urls.py)
- We will add a button using `a tag` inside [student-list.html](./school_app/templates/student-list.html) : `<a href="{% url 'add_student' %}" class="btn btn-primary">Add Student</a>`
- Now we will be able to add data from frontend

---
[⬆️ Go to Context](#context)
