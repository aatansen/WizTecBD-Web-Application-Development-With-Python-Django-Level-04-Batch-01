# Context

- [Context](#context)
  - [Django Template Setup](#django-template-setup)
  - [Context Data](#context-data)
  - [Navigation Page using URL name](#navigation-page-using-url-name)

## Django Template Setup

- Create a folder [templates](./templates/) in project base directory where [manage.py](./manage.py) is
- Add this [templates](./templates/) path in [settings.py](./firstProject/settings.py)

  ```py
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [BASE_DIR,"templates"],
          ...
      },
  ]
  ```

- Now create a function inside [views.py](./firstProject/views.py) `home_page()` by importing `render` function from `django.shortcuts` using *selective import* and render [home.html](./templates/home.html)

  ```py
  from django.shortcuts import render

  def home_page(request):
    return render(request,'home.html')
  ```

- Add it inside `urlpatterns`

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

## Context Data

- Inside the `home_page()` function, create a dictionary and pass it to the template using `context`.

  ```py
  from django.shortcuts import render

  def home_page(request):
    info = {
      "name": "Tansen",
      "address": "Dhaka"
    }
    return render(request, 'home.html', context=info)
  ```

- Now inside [home.html](./templates/home.html) use Django Template Language (DTL) to display data passed from the view.
- Variables are accessed using double curly braces `{{ }}`.

  ```jinja
  <h1>Hello {{ name }}</h1>
  <h1>from {{ address }}</h1>
  ```

## Navigation Page using URL name

- Create another function `about_page()`
- and render [about.html](./templates/about.html)

  ```py
  def about_page(request):
    return render(request,'about.html')
  ```

- Add it inside `urlpatterns` in [urls.py](./firstProject/urls.py)

  ```py
  from django.contrib import admin
  from django.urls import path
  from . import views

  urlpatterns = [
      ...
      path('about/',views.about_page,name='about'),
  ]
  ```

- Use the URL name in the template for navigation

  ```jinja
  <a href="{% url 'home' %}">Home</a>
  <a href="{% url 'about' %}">About</a>
  ```

> [!NOTE]
>
> - We will add this in both [home.html](./templates/home.html) and [about.html](./templates/about.html)
>
> - Note that we will do this in better way in future by learning template mastering
