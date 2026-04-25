# Context

- [Context](#context)
  - [Django Form](#django-form)
    - [Create Model](#create-model)
    - [Add Data From Admin Page](#add-data-from-admin-page)
    - [Create A HTML Page To View It](#create-a-html-page-to-view-it)
    - [Create Django Form](#create-django-form)

## Django Form

### Create Model

- Create a model in [models.py](./form_app/models.py)

  ```py
  class ProductModel(models.Model):
    product_name=models.CharField(max_length=100,null=True)
    product_price=models.FloatField(null=True)
    product_description=models.TextField(null=True)
    product_qty=models.PositiveIntegerField(null=True)

    PRODUCT_CATEGORY=[
      ('Electic','Electic'),
      ('Cloth','Cloth'),
      ('Food','Food'),
    ]
    product_cat=models.CharField(choices=PRODUCT_CATEGORY,null=True)
    product_img=models.ImageField(upload_to='media/product_imgs',null=True)

    def __str__(self):
      return f'{self.product_name}'
  ```

  - `null=True` in every field to avoid error during model field `modify / alter`
  - Here new choice field is added where we have a list `PRODUCT_CATEGORY` and inside that we have tuple
    - Left value will be used in code
    - Right value will be visible to user in frontend

      > For error free code we use both the same

  - Another new field is image field where we use `ImageField` and `upload_to`
    - We have to install new package [pillow](https://pypi.org/project/pillow/) in order to make the image field work
    - We need to setup this from official docs: "[Serving files uploaded by a user during development](https://docs.djangoproject.com/en/6.0/howto/static-files/#serving-files-uploaded-by-a-user-during-development)"
    - Copy the `MEDIA_ROOT`
    - Put it inside project [urls.py](./form_project/urls.py)

      ```py
      ...
      from django.conf import settings
      from django.conf.urls.static import static

      urlpatterns = [
          ...
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```

- Run migration commands
- Register model in [admin.py](./form_app/admin.py)

---
[⬆️ Go to Context](#context)

### Add Data From Admin Page

- Now we will add data from our admin page just to ensure is it working properly or not

---
[⬆️ Go to Context](#context)

### Create A HTML Page To View It

- As usual create HTML files as below and apply bootstrap and [Django Template Inheritance](https://docs.djangoproject.com/en/6.0/ref/templates/language/)

  ```txt
  📁 templates
  ├── 📁 master
  │   ├── 🌐 base.html
  │   └── 🌐 nav.html
  └── 🌐 product-list.html
  ```

- Create a function in [views.py](./form_app/views.py)
- Add URL pattern in [urls.py](./form_app/views.py)
  > Make sure App's [urls.py](./form_app/urls.py) is included in Project's [urls.py](./form_project/urls.py)
- Now to show image in [product-list.html](./form_app/templates/product-list.html) we used condition

  ```jinja
  <td>
    {% if data.product_img %}
    <img src="{{data.product_img.url}}" alt="product image" width="20">
    {% else %}
    No image
    {% endif %}
  </td>
  ```

---
[⬆️ Go to Context](#context)

### Create Django Form

- Create [forms.py](./form_app/forms.py) in [app directory](./form_app/)

  ```py
  from django import forms
  from form_app.models import ProductModel

  class ProductForm(forms.ModelForm):
    class Meta:
      model=ProductModel
      fields='__all__'
  ```

- Create a function in [views.py](./form_app/views.py)

  ```py
  def product_add(request):
    # to show the form in html page
    form_data=ProductForm()
    context={
      'form_data':form_data
    }
    return render(request,'product-add.html',context=context)
  ```

- Create [product-add.html](./form_app/templates/product-add.html)

  ```jinja
  {% extends 'master/base.html' %}

  {% block content %}
  <h1>Add product</h1>

  <form method="POST" enctype="multipart/form-data">
  {% csrf_token %}

    {{form_data}}

    <button type="submit" class="btn btn-primary">Add Product</button>
  </form>

  {% endblock content %}
  ```

  - In here we use only `form_data` key from our views which we sent as a context in dictionary
  - `method` is `POST` and new `enctype` is `multipart/form-data` we use this to accept image/file
- Add URL pattern in [urls.py](./form_app/urls.py)
- Add this URL in [product-list.html](./form_app/templates/product-list.html) `Add Product` button using `a tag`
- Now we are going to update our `product_add` function to accept user input data from the form

  ```py
  def product_add(request):
    # to save the form data in database
    if request.method == 'POST':
      form_data=ProductForm(request.POST, request.FILES)
      if form_data.is_valid():
        form_data.save()
        return redirect('product_list')

    # to show the form in html page
    form_data=ProductForm()
    context={
      'form_data':form_data
    }
    return render(request,'product-add.html',context=context)
  ```

  - Look carefully there is two part, last part `to show the form in html page` we already used this and in `to save the form data in database` part is used to get data from [product-add.html](./form_app/templates/product-add.html) and save in database

> [!IMPORTANT]
>
> - A new package [pillow](https://pypi.org/project/pillow/) is required to make the image field work
> - You must use `enctype="multipart/form-data"` in form to accept image/file
> - Make sure you used `ProductForm(request.POST, request.FILES)` in backend otherwise you wont be able to save data/files/image

---
[⬆️ Go to Context](#context)
