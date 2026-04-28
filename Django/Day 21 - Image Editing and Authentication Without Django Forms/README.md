# Context

- [Context](#context)
  - [Image Editing Without Django Forms](#image-editing-without-django-forms)
  - [Authentication Without Django Forms](#authentication-without-django-forms)
    - [Registration](#registration)
    - [Login](#login)
    - [Logout](#logout)
    - [Decorators](#decorators)

> [!NOTE]
>
> - To follow along you must have add data and view it in a table
> - Make sure all form you created is without using Django form
> - We will start from the table by adding action column where `edit` action will be cover

## Image Editing Without Django Forms

- Create edit function `student_edit` in [views.py](./auth_app/views.py)
- Add URL pattern in [urls.py](./auth_app/urls.py)
- Add URL name in edit button `a tag` in [student-list.html](./auth_app/templates/student-list.html)
- Now usually we create edit page form exact same as add form HTML only difference is we add `value` attribute in edit form
- Now for image we won't see the selected image in edit page when we use normal HTML form
- We will manually show it using `img` tag in edit page [student-edit.html](./auth_app/templates/student-edit.html)

  ```jinja
  <label for="" class="form-label">Profile Pic</label>
  <input type="file" class="form-control" name="profile_pic" value="{{student_data.profile_pic}}">
  <p>Current Image:</p>
  {% if student_data.profile_pic %}
  <img src="{{student_data.profile_pic.url}}" alt="" width="30px">
  {% else %}
  No image
  {% endif %}
  ```

- Now in [views.py](./auth_app/views.py) function `student_edit` we need to handle when user don't update image we have to check the image we get from the HTML form

  - Not recommended way (using the model directly)

    ```py
    def student_edit(request,id):
      student_data=StudentModel.objects.get(id=id)

      # Get data from html page form
      if request.method=="POST":
        name=request.POST.get('name')
        profile_pic=request.FILES.get('profile_pic')

        # we can do this but not recommended
        if not profile_pic:
          profile_pic=student_data.profile_pic
        StudentModel(
          id=id,
          name=name,
          profile_pic=profile_pic,
        ).save()

        return redirect('student_list')
    ```

  - Here is the proper way to do this

    ```py
    def student_edit(request,id):
      student_data=StudentModel.objects.get(id=id)

      # Get data from html page form
      if request.method=="POST":
        name=request.POST.get('name')
        profile_pic=request.FILES.get('profile_pic')

        # update the data to database
        student_data.name=name
        if profile_pic:
          student_data.profile_pic=profile_pic
        student_data.save()
        return redirect('student_list')
    ```

> [!IMPORTANT]
>
> - When we create form without using Django form it won't show the current image from the database in the HTML page automatically, we have to manually show it using `img` tag
> - In our edit function we have to handle when user don't update image, So we have to make condition only update the database if we get the updated image from the user
> - When we directly use Model to update data we have to pass `id` and every fields, otherwise it won't work
> - When we access our model data using `.` and we can update whichever fields we want no need to update every field

---
[⬆️ Go to Context](#context)

## Authentication Without Django Forms

- To follow up with our current student page we make a condition like we can see the student table if we logged in so in [student-list.html](./auth_app/templates/student-list.html) we put `user.is_authenticated` in if condition
- We will use `User` to authenticate user
  - This user actually already created inside `from django.contrib.auth.models`
  - This is also where our superuser created
    - `from django.contrib.auth.models import User`
  - To see the available fields we can login to admin page and see those fields
    - `Username` | `username`
    - `Password` | `password`
    - `First name` | `first_name`
    - `Last name` | `last_name`
    - `Email address` | `email`

---
[⬆️ Go to Context](#context)

### Registration

- Create a HTML page [register.html](./auth_app/templates/register.html)
- Now create a function in [views.py](./auth_app/views.py) for registration

  ```py
  def register_page(request):
    if request.method=="POST":
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')
      c_password=request.POST.get('c_password')

      if password==c_password:
        User.objects.create_user(
          username=username,
          email=email,
          password=password
        )
        return redirect('login_page')

    return render(request,'register.html')
  ```

  - `User` here is imported by `from django.contrib.auth.models import User`
  - We used `.create_user` ir order to create user properly if we use `.create` only it won't save password as hash and login won't work
- Now add URL pattern in [urls.py](./auth_app/urls.py)
- Add this URL name like `Already have an account?` `a tag` in login page [login-page.html](./auth_app/templates/login-page.html)

---
[⬆️ Go to Context](#context)

### Login

- Now we will make [login.html](./auth_app/templates/login-page.html)
- Create login function in [views.py](./auth_app/views.py)

  ```py
  def login_page(request):
    if request.method=="POST":
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=authenticate(
        request,
        username=username,
        password=password,
      )
      if user:
        login(request,user)
        return redirect('student_list')
      else:
        print("Not Authorize")

    return render(request,'login-page.html')
  ```

  - In here we authenticate the user to login and in else condition we use print but later on we will learn django messages to show message to user in frontend
  - `authenticate` and `login` are imported by `from django.contrib.auth import authenticate,login`
- Now add URL pattern in [urls.py](./auth_app/urls.py)
- Add this URL name like `Don't have an account?` `a tag` in register page [register.html](./auth_app/templates/register.html)
- Also add the URL name in navbar
- Now we can access our login user by `{{user.username}}` in this way we can also check if user is login or not to restrict a page view `{{user.is_authenticated}}`

---
[⬆️ Go to Context](#context)

### Logout

- Now let's do the log out
- Create a function in [views.py](./auth_app/views.py)

  ```py
  def signout(request):
    logout(request)
    return redirect('login_page')
  ```

  - Note that we can't use `logout` name in function cause there is already a function we imported so we named it `signout`
  - We import this `logout` by `from django.contrib.auth import logout`
- Add URL pattern in [urls.py](./auth_app/urls.py)
- Now let's put this URL name using condition in navbar
  - When login user will see logout button otherwise it will show login in navbar

    ```jinja
    <li class="nav-item">
      {% if user.is_authenticated %}
      <a class="nav-link active" aria-current="page" href="{% url 'signout' %}">Logout</a>
      {% else %}
      <a class="nav-link active" aria-current="page" href="{% url 'login_page' %}">Login</a>
      {% endif %}
    </li>
    ```

---
[⬆️ Go to Context](#context)

### Decorators

- We can restrict a page using decorator `login_required`

  ```py
  from django.contrib.auth.decorators import login_required

  @login_required
  def student_edit(request,id):
    ...

  @login_required
  def student_add(request):
    ...
  ```

  - We already restricted [student-list.html](./auth_app/templates/student-list.html) page using `user.is_authenticated`
  - In here we used decorator to protect the view of those pages by using decorator and decorators are used `@` sign at to of the function view you want to restrict
- Now where will a user go if he is not login and try to access those restricted pages, we have to mention that page in [settings.py](./auth_project/settings.py) at the end line

  ```py
  LOGIN_URL='login_page'
  ```

  - here `login_page` is the URL name of login page

> [!IMPORTANT]
>
> - When we use `User` to authenticate we can only use it's predefined field, we can't extend it. Later we will learn `AbstractUser` to extend fields. The difference is when we use `User` we don't need to create model but when we use `AbstractUser` we have to create Model where we will mention our own fields
> - When we create a user we use `.create_user()` instead of `.create()` otherwise password won't be hashed and login won't work
> - We can create ustom decorators too

---
[⬆️ Go to Context](#context)
