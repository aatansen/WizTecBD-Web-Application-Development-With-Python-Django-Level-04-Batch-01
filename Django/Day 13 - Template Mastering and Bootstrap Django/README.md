# Context

- [Context](#context)
  - [Basic Django Template Mastering](#basic-django-template-mastering)

## Basic Django Template Mastering

- Create a project

  ```sh
  django-admin startproject templateMastering .
  ```

- Create [templates](./templates/) folder inside project directory where [manage.py](./manage.py) is
- Add template path in [settings.py](./templateMastering/settings.py)

  ```py
  TEMPLATES = [
      {
          ...
          'DIRS': [BASE_DIR,'templates'],
          ...
      },
  ]
  ```

- Create [home.html](./templates/home.html), [about.html](./templates/about.html), [nav.html](./templates/nav.html), [footer.html](./templates/footer.html) all inside [templates](./templates/)
- Create two function for [home.html](./templates/home.html) and [about.html](./templates/about.html) in [views.py](./templateMastering/views.py)

  ```py
  from django.shortcuts import render

  def home_page(request):
    return render(request,'home.html')

  def about_page(request):
    return render(request,'about.html')
  ```

- Add `urlpatterns` inside [urls.py](./templateMastering/urls.py)

- Now two more template left which is [nav.html](./templates/nav.html) and [footer.html](./templates/footer.html)
- We will include them inside our [home.html](./templates/home.html) and [about.html](./templates/about.html) using Django `include` tag

> [!NOTE]
>
> - We use the URL name in the [nav.html](./templates/nav.html) for navigation

- Using the [include tag](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#include)

  ```jinja
  {% include 'nav.html' %}

  <h1>Home page</h1>

  {% include 'footer.html' %}
  ```

  - Do the same in [about.html](./templates/about.html)

---
[⬆️ Go to Context](#context)
