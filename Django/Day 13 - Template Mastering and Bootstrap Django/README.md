# Context

- [Context](#context)
  - [Basic Django Template Mastering](#basic-django-template-mastering)
  - [Advanced Django Template Mastering](#advanced-django-template-mastering)
  - [Bootstrap in Django Template](#bootstrap-in-django-template)

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

- Create [home.html](./templates/home.html), [about.html](./templates/about.html), [nav.html](./templates/master/nav.html), [footer.html](./templates/master/footer.html) all inside [templates](./templates/)
- Create two function for [home.html](./templates/home.html) and [about.html](./templates/about.html) in [views.py](./templateMastering/views.py)

  ```py
  from django.shortcuts import render

  def home_page(request):
    return render(request,'home.html')

  def about_page(request):
    return render(request,'about.html')
  ```

- Add `urlpatterns` inside [urls.py](./templateMastering/urls.py)

- Now two more template left which is [nav.html](./templates/master/nav.html) and [footer.html](./templates/master/footer.html)
- We will include them inside our [home.html](./templates/home.html) and [about.html](./templates/about.html) using Django `include` tag

> [!NOTE]
>
> - We use the URL name in the [nav.html](./templates/master/nav.html) for navigation

- Using the [include tag](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#include)

  ```jinja
  {% include 'nav.html' %}

  <h1>Home page</h1>

  {% include 'footer.html' %}
  ```

  - Do the same in [about.html](./templates/about.html)

---
[⬆️ Go to Context](#context)

## Advanced Django Template Mastering

- We will create a [master directory](./templates/master/) for shared template where `base.html` is main `layout` and others repeated content HTML files (e.g: `nav.html`, `footer.html`) are `partials`

  ```txt
  📁 templates
  ├── 📁 master
  │   ├── 🌐 base.html
  │   ├── 🌐 footer.html
  │   └── 🌐 nav.html
  ├── 🌐 about.html
  └── 🌐 home.html
  ```

- We may see more structure like this in complex projects

  ```txt
  📁 project_root
  ├── 📁 project_name
  │   ├── settings.py
  │   ├── urls.py
  │   └── ...
  │
  ├── 📁 templates                # Global templates (shared across apps)
  │   ├── 📁 layouts              # Base/layout files
  │   │   └── 🌐 base.html
  │   │
  │   ├── 📁 partials             # Reusable components
  │   │   ├── 🌐 nav.html
  │   │   └── 🌐 footer.html
  │   │
  │   ├── 🌐 home.html
  │   └── 🌐 about.html
  │
  ├── 📁 app1
  │   ├── 📁 templates
  │   │   └── 📁 app1             # Namespaced (VERY important)
  │   │       ├── 🌐 index.html
  │   │       └── 🌐 detail.html
  │   └── ...
  │
  ├── 📁 app2
  │   ├── 📁 templates
  │   │   └── 📁 app2
  │   │       └── 🌐 page.html
  │   └── ...
  │
  └── manage.py
  ```

- Now let's follow our simple structure and fill out [base.html](./templates/master/base.html)

  ```jinja
  <body>

    {% include 'master/nav.html' %}


    {% block content %}

    {% endblock content %}

    {% include 'master/footer.html' %}

  </body>
  ```

  - Here we use another new `block tag` which is used for [Django Template Inheritance](https://docs.djangoproject.com/en/6.0/ref/templates/language/#template-inheritance)
  - It is used as replaceable section in a base template that child templates can override.
- Now we have to modify our [home.html](./templates/home.html), [about.html](./templates/about.html)

  ```jinja
  {% extends 'master/base.html' %}

  {% block content %}

  <h1>Home page</h1>

  {% endblock content %}
  ```

  - Do the same for [about.html](./templates/about.html)
  - We can see another new [extends tag](https://docs.djangoproject.com/en/6.0/ref/templates/builtins/#extends) which is used to connect parent ([base.html](./templates/master/base.html)) and child ([home.html](./templates/home.html) / [about.html](./templates/about.html))
  - Also we can see the use of `block tag` which was empty in parent ([base.html](./templates/master/base.html)) but in child ([home.html](./templates/home.html)) it is fill out with its own contents and this same thing done in [about.html](./templates/about.html)

- Now let's say we want to see title of each page dynamically
  - Modify title [base.html](./templates/master/base.html) using `block tag`

    ```jinja
    <title> {% block title_block %} {% endblock title_block %}</title>
    ```

  - Now use it in [home.html](./templates/home.html) and [about.html](./templates/about.html)

    ```jinja
    {% extends 'master/base.html' %}

    {% block title_block %}
      Home
    {% endblock title_block %}

    {% block content %}

    <h1>Home page</h1>

    {% endblock content %}
    ```

    - Do the same in [about.html](./templates/about.html)

---
[⬆️ Go to Context](#context)

## Bootstrap in Django Template

> [!NOTE]
>
> - We can either use the CDN or download and use it
> - We will use CDN

- Get [Bootstrap quick start template](https://getbootstrap.com/docs/5.3/getting-started/introduction/#quick-start)
- Use it in [base.html](./templates/master/base.html)
- Now also modify [nav.html](./templates/master/nav.html) and use [navbar component](https://getbootstrap.com/docs/5.3/components/navbar/#nav) from bootstrap
- We can do the same for footer also using [footer component](https://getbootstrap.com/docs/5.3/components/card/#header-and-footer)

---
[⬆️ Go to Context](#context)
