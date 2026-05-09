# Context

- [Context](#context)
  - [Demonstration-02(To-Do List Application)](#demonstration-02to-do-list-application)
    - [Create Project](#create-project)
    - [Create App](#create-app)
    - [Create Models](#create-models)
    - [Initialize Database](#initialize-database)
    - [Superuser Create](#superuser-create)
    - [Create Django Form \& Crispy Apply](#create-django-form--crispy-apply)
    - [Templates And Non-CDN Bootstrap Setup](#templates-and-non-cdn-bootstrap-setup)
      - [Non-CDN Bootstrap Setup](#non-cdn-bootstrap-setup)
      - [Templates Setup](#templates-setup)
    - [Register Page](#register-page)
    - [Login Page](#login-page)
    - [Logout](#logout)
    - [Task List Page](#task-list-page)
    - [Task Add \& Update Page](#task-add--update-page)
      - [Task Add Page](#task-add-page)
      - [Task Update Page](#task-update-page)
    - [View Task Page](#view-task-page)
    - [Delete Task](#delete-task)

## Demonstration-02(To-Do List Application)

**Project Specification:**

> Build a Django project for a To-Do List Application. Anyone can create their account into this application, then users can create, update, and delete tasks. You need to create model to store the To-Do information. Define the fields for this model. Apply authentication(Login, Register, Logout).

- After running the server opens Registration Page. From this page user can register their account using these fields (username, full_name, email, password, confirm_password). This data will be stored on the Custom user model.
- Then, from the login page then can logged-in their account using the username and password.

**Project Setup:**

- Project Name: `todo_project`
- App Name: `tasks`
- Model: `CustomUserInfoModel`, `TaskModel`

**Defining the following fields for the `CustomUserInfoModel`:**

- `username`, `full_name`, `email`, `password`, `confirm_password`

> Note: User Model must be `CustomUser Model` not `User Model`

**Defining the following fields for the Task Model:**

- `title`, `description`, `status`(`Pending`, `InProgress`, `Completed`, `Canceled`), `due_date`, `created_at`, `updated_at`

> **Note:** Apply Django form to create new and update task.

**Templates and Navigation:**

- Create a master template with the navigation links:
  - **Register**
  - **Login**
  - **Logout**
  - **Home:** Create a homepage to show welcome message with the username.
  - **Add Task:** From this page user can create their `task`
  - **Task List:** Display all the tasks in a table with these columns: Title, Description, Due Date.
  - **Task Detail:** Implement a detail view to show individual task information.

---
[⬆️ Go to Context](#context)

> [!NOTE]
> Create and activate `.venv` and install `django` then follow along

### Create Project

- Creating project `todo_project`

  ```sh
  django-admin startproject todo_project .
  ```

---
[⬆️ Go to Context](#context)

### Create App

- Creating app `tasks`

  ```sh
  py manage.py startapp tasks
  ```

  - Add app name inside `INSTALLED_APPS` in [settings.py](./todo_project/settings.py)

---
[⬆️ Go to Context](#context)

### Create Models

- Creating Model `CustomUserInfoModel` and `TaskModel` in [models.py](./tasks/models.py)

  ```py
  from django.db import models
  from django.contrib.auth.models import AbstractUser

  # Create your models here.
  class CustomUserInfoModel(AbstractUser):
    full_name=models.CharField(max_length=100,null=True)

    def __str__(self):
      return f'{self.full_name}'
  ```

  - Question mentioned total 5 fields in `CustomUserInfoModel` model:
    - `username`,
    - `full_name`,
    - `email`,
    - `password`,
    - `confirm_password`
  - But we only mentioned `full_name` here cause other `username`, `email`, `password` already in base user model (`from django.contrib.auth.models import User`) and `AbstractUser` model is using base user model to extends our fields like `full_name` and finally another field in the question is `confirm_password` this field is actually mentioned just to add it in the form to ensure user inputted correct password in password field which we check in the backend `views` function
- To make this model `CustomUserInfoModel` works we have to make a variable `AUTH_USER_MODEL` in [settings.py](./todo_project/settings.py) and write it in this order: `app_name.model_name`

  ```py
  # custom user model
  AUTH_USER_MODEL='tasks.CustomUserInfoModel'
  ```

- Now we will create `TaskModel`

  ```py
  class TaskModel(models.Model):
    title=models.CharField(max_length=100,null=True)
    description=models.TextField(null=True)

    STATUS=[
      ('Pending','Pending'),
      ('InProgress','InProgress'),
      ('Completed','Completed'),
      ('Canceled','Canceled'),
    ]
    status=models.CharField(choices=STATUS,max_length=100,null=True)
    due_date=models.DateField(null=True)
    created_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
    created_by=models.ForeignKey(CustomUserInfoModel,on_delete=models.CASCADE,null=True)

    def __str__(self):
      return f'{self.title}'
  ```

  - New argument in `DateField` which is `auto_now_add` and `auto_now` by the field name we can see when to use which one
  - We have created a relationship with our custom model here in `created_by` this `ForeignKey` relation is called *One-to-Many / Many-to-One*. We used this cause one user can create many task
  - `on_delete=models.CASCADE` means when a user is deleted all the task created by that user will also be deleted

- Now register those two model in [admin.py](./tasks/admin.py)

  ```py
  from django.contrib import admin
  from tasks.models import CustomUserInfoModel,TaskModel
  # Register your models here.

  admin.site.register(
    [
      CustomUserInfoModel,
      TaskModel,
    ]
  )
  ```

---
[⬆️ Go to Context](#context)

### Initialize Database

- Run both initial and app migration commands

  Initial migration commands

  ```sh
  py manage.py makemigrations
  ```

  ```sh
  py manage.py migrate
  ```

  App migration commands

  ```sh
  py manage.py makemigrations tasks
  ```

  ```sh
  py manage.py migrate tasks
  ```

---
[⬆️ Go to Context](#context)

### Superuser Create

- Create `superuser`

  ```sh
  py manage.py createsuperuser
  ```

> At this point we will add data in our database using admin page just to ensure model are working properly

---
[⬆️ Go to Context](#context)

### Create Django Form & Crispy Apply

- Now we will create [forms.py](./tasks/forms.py) and make `TaskForm`

  ```py
  from django.forms import fields
  from django import forms
  from tasks.models import TaskModel

  class TaskForm(forms.ModelForm):
    class Meta:
      model=TaskModel
      fields='__all__'
      exclude=['created_by']
      widgets={
        'due_date':forms.DateInput(attrs={
          'class':'form-control',
          'type':'date',
        })
      }
  ```

  - In here we make a `TaskForm` as usual, but widget is used to make sure date field shows properly in the HTML page
  - We excluded `created_by` field because it won't be filled by user, we will make logic in backend to fill it
  - For other fields we will use [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/)

    ```sh
    pip install crispy-bootstrap5
    ```

    Add this inside `INSTALLED_APPS` in [settings.py](./todo_project/settings.py) file at end line

    ```py
    # bootstrap 5
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    ```

    In each HTML form page we have to load the form tags

    ```jinja
    {% load crispy_forms_tags %}
    ```

    And in form variable

    ```jinja
    {{form_data | crispy}}
    ```

---
[⬆️ Go to Context](#context)

### Templates And Non-CDN Bootstrap Setup

#### Non-CDN Bootstrap Setup

- Download [Bootstrap 5](https://getbootstrap.com/docs/5.3/getting-started/download/)
- Unzip the file `bootstrap-5.3.8-dist.zip` and copy these two files
  - `css/bootstrap.min.css`
  - `js/bootstrap.bundle.min.js`
- Create a folder [static](./tasks/static/) inside [App](./tasks/) directory and organize those two files as below

  ```txt
  📁 static
  └── 📁 bootstrap
      ├── 📁 css
      │   └── 🌐 bootstrap.min.css
      └── 📁 js
          └── ⚙️ bootstrap.bundle.min.js
  ```

  - In [base.html](./tasks/templates/master/base.html) at top we have to load this

    ```jinja
    {% load static %}
    ```

  - And before `head` end tag add this line for `bootstrap.min.css`

    ```jinja
    <link rel="stylesheet" href="{% static 'bootstrap/css/bootstrap.min.css' %}">
    ```

  - And before `body` end tag add this line for `bootstrap.bundle.min.js`

    ```jinja
    <script src="{% static 'bootstrap/js/bootstrap.bundle.min.js' %}"></script>
    ```

---
[⬆️ Go to Context](#context)

#### Templates Setup

- Create a structure like this

  ```txt
  📁 templates
  ├── 📁 master
  │   ├── 🌐 base-form.html (for add task and update task using django form)
  │   ├── 🌐 base.html
  │   └── 🌐 nav.html
  ├── 🌐 home-page.html
  ├── 🌐 login-page.html
  ├── 🌐 register-page.html
  ├── 🌐 task-detail.html
  └── 🌐 task-list.html
  ```

---
[⬆️ Go to Context](#context)

### Register Page

- Now let's create [register-page.html](./tasks/templates/register-page.html) get [a bootstrap form](https://getbootstrap.com/docs/5.3/forms/overview/#overview)
- Create a function `register_page` in [views.py](./tasks/views.py)
- Add URL path in [urls.py](./tasks/urls.py), according to question home page will show the register page, so path route should be `""` empty

> Make sure [urls.py](./tasks/urls.py) of app is included in project [urls.py](./todo_project/urls.py)

---
[⬆️ Go to Context](#context)

### Login Page

- Now let's create [login-page.html](./tasks/templates/login-page.html) get [a bootstrap form](https://getbootstrap.com/docs/5.3/forms/overview/#overview)
- Create a function `login_page` in [views.py](./tasks/views.py)
- Add URL path in [urls.py](./tasks/urls.py)

### Logout

- Create a function `signout` in [views.py](./tasks/views.py)

  ```py
  def signout(request):
    logout(request)
    return redirect('login_page')
  ```

- Add URL path in [urls.py](./tasks/urls.py)

---
[⬆️ Go to Context](#context)

### Task List Page

- We have added some data using admin page so we can view those in this page as a table
- Create a table in [task-list.html](./tasks/templates/task-list.html) with action column for `view`,`update`,`delete`
- Create a function in [views.py](./tasks/views.py)

  ```py
  @login_required
  def task_list(request):
    task_data=TaskModel.objects.filter(created_by=request.user)

    context={
      'task_data':task_data
    }
    return render(request,'task-list.html',context=context)

  ```

  - In here we used `filter` query to get all the task created by that user
  - We used decorator `@login_required` which is imported by `from django.contrib.auth.decorators import login_required`, it is used to protect a view. In [settings.py](./todo_project/settings.py) we have to add `LOGIN_URL` variable and store the name of our login page URL in order to make decorator work

    ```py
    # decorator URL
    LOGIN_URL='login_page'
    ```

- Add URL path in [urls.py](./tasks/urls.py)

---
[⬆️ Go to Context](#context)

### Task Add & Update Page

- For both page we will use single HTML page [base-form.html](./tasks/templates/master/base-form.html) cause both are exact same

---
[⬆️ Go to Context](#context)

#### Task Add Page

- We already created the form in [forms.py](./tasks/forms.py) for task model
- Now we will create a function in [views.py](./tasks/views.py)

  ```py
  @login_required
  def task_add(request):

    # to save form data to database
    if request.method=="POST":
      form_data=TaskForm(request.POST)
      if form_data.is_valid():
        data=form_data.save(commit=False)
        data.created_by=request.user
        data.save()
        return redirect('task_list')

    # to show the form
    form_data=TaskForm()
    context={
      'form_data':form_data,
      'form_title':'Add Task Page',
      'form_btn':'Add Task',
    }
    return render(request,'master/base-form.html',context)
  ```

  - `@login_required` decorator used to protect the view from unauthorized user
  - In here we used `commit=False` to hold it and assign the current login user to the model then save it
  - As we are using single form for add and update so we are sending `form_title` and `form_btn` also in the context

- Add URL path in [urls.py](./tasks/urls.py)
- Add name URL in Add Task button in [task-list.html](./tasks/templates/task-list.html)

---
[⬆️ Go to Context](#context)

#### Task Update Page

- It is same as task add
- Create a function in [views.py](./tasks/views.py)

  ```py
  @login_required
  def task_edit(request,id):
    task_data=get_object_or_404(TaskModel,id=id)
    # to save form data to database
    if request.method=="POST":
      form_data=TaskForm(request.POST,instance=task_data)
      if form_data.is_valid():
        data=form_data.save(commit=False)
        data.created_by=request.user
        data.save()
        return redirect('task_list')

    # to show the form
    form_data=TaskForm(instance=task_data)
    context={
      'form_data':form_data,
      'form_title':'Update Task Page',
      'form_btn':'Update Task',
    }
    return render(request,'master/base-form.html',context)
  ```

  - As same as add task function only difference is we are using `id` to get the specific data and `instance` here to show the current model data in the form, so user can see it during editing

- Add URL path in [urls.py](./tasks/urls.py)
- Add name URL in Edit Task action in [task-list.html](./tasks/templates/task-list.html)

---
[⬆️ Go to Context](#context)

### View Task Page

- Now we will create a function in [views.py](./tasks/views.py)

  ```py
  def task_detail(request,id):
    task_data=get_object_or_404(TaskModel,id=id)

    context={
      'task_data':task_data,
    }
    return render(request,'task-detail.html',context=context)
  ```

- Add URL path in [urls.py](./tasks/urls.py)
- Add name URL in View Task action in [task-list.html](./tasks/templates/task-list.html)
- Access variable using `{{}}`

---
[⬆️ Go to Context](#context)

### Delete Task

- Now we will create a function in [views.py](./tasks/views.py)

  ```py
  def task_delete(request,id):
    task_data=get_object_or_404(TaskModel,id=id)
    task_data.delete()
    return redirect('task_list')
  ```

- Add URL path in [urls.py](./tasks/urls.py)
- Add name URL in Delete Task action in [task-list.html](./tasks/templates/task-list.html)

> [!IMPORTANT]
>
> - If the question mentioned `User Model` you don't need to create model in models.py for user. Cause `User Model` is *built-in* which we just import in our `views.py` to store data in it `from django.contrib.auth.models import User`
> - If the question mentioned `Custom User Model` then you must create a model in `models.py` by inherits the `AbstractUser` which is used to extend the fields for example `user_type` or `full_name` etc
> - Must remember that while creating `Custom User Model` we don't write `models.Model` we write `AbstractUser` which is imported by `from django.contrib.auth.models import AbstractUser`
> - When we have `Custom User Model` we must do the *initial migrations commands* after model create otherwise `User Model` and `Custom User Model` conflict will occur
> - We use `widgets` in `forms.py` to customize HTML form page or show some of the field properly like `date field`
> - We used `{{user.is_authenticated}}` to verify if a user is logged in or not in the frontend HTML pages

---
[⬆️ Go to Context](#context)
