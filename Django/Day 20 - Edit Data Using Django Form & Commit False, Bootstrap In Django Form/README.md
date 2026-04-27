# Context

- [Context](#context)
  - [Edit Data Using Django Form](#edit-data-using-django-form)
  - [Django Form Commit False](#django-form-commit-false)
  - [Bootstrap In Django Form](#bootstrap-in-django-form)
  - [Radio Select And Date Field In Django Form](#radio-select-and-date-field-in-django-form)

## Edit Data Using Django Form

- Creating product edit function and HTML page
  - Create a function `product_edit` in [views.py](./form_app/views.py)
  - This function render a HTML page [product-edit.html](./form_app/templates/product-edit.html) so create it
  - Add URL pattern in [urls.py](./form_app/urls.py)
  - Create action column in [product-list.html](./form_app/templates/product-list.html)
  - Add URL of `product_edit` in edit button action URL
- The function `product_edit` in [views.py](./form_app/views.py) is similar to `product_add` function and the page [product-edit.html](./form_app/templates/product-edit.html) also same as [product-add.html](./form_app/templates/product-add.html)
- `product_add` function

  ```py
  def product_add(request):
    # to show the form in html page
    form_data=ProductForm()
    context={
      'form_data':form_data
    }
    return render(request,'product-add.html',context=context)
  ```

  - In `product_add` function to show the form we write this part and sent the data as `context`
- `product_edit` function

  ```py
  def product_edit(request,id):
    product_data=ProductModel.objects.get(id=id)
    # to show the form in html page
    form_data=ProductForm(instance=product_data)
    context={
      'form_data':form_data
    }
    return render(request,'product-edit.html',context=context)
  ```

  - We can see the function `product_edit` is exact similar to `product_add` function only difference is we are providing model data to it using `instance` so that `product_edit` can show the existing data of that individual

- Now to save data we will update the `product_edit` function

  ```py
  def product_edit(request,id):
    product_data=ProductModel.objects.get(id=id)

    # to update data in database
    if request.method == 'POST':
      form_data=ProductForm(request.POST,request.FILES,instance=product_data)
      if form_data.is_valid():
        form_data.save()
        return redirect('product_list')
    ...
    return render(request,'product-edit.html',context=context)
  ```

  - Here we can see just like saving data in `product_add` but we include `instance` here, so it can update that specific individual data

---
[⬆️ Go to Context](#context)

## Django Form Commit False

- Now let's say we have a situation where we have a field in our model that we fill it not by user
  - For example `Total amount`
  - Let's update our model and add this field

    ```py
    class ProductModel(models.Model):
      ...
      product_total_amount=models.FloatField(null=True)
      ...
      def __str__(self):
        return f'{self.product_name}'
    ```

      > Make sure to run migrations command with app name

  - Now this field will be filled by us in backend
  - So we have to remove this from the form using `exclude` in [forms.py](./form_app/forms.py)

    ```py
    class ProductForm(forms.ModelForm):
      class Meta:
        model=ProductModel
        fields='__all__'
        exclude=['product_total_amount']
    ```

  - Now we have to update `product_edit` function

    ```py
    ...
    if form_data.is_valid():
      data=form_data.save(commit=False)
      data.product_total_amount=data.product_price*data.product_qty
      data.save()
      return redirect('product_list')
    ...
    ```

    - In here we used `commit=False` which is used to hold the save in `data` variable before doing an operation
    - Then we access our model field using `.` and calculate the `product_total_amount` and finally save it

  - Now we will update our [product-list.html](./form_app/templates/product-list.html) and add the total amount in the column

> [!IMPORTANT]
>
> - We use `commit=False` to hold the save before doing an operation (it could be calculation or assigning status or anything)
> - If you have a field in your model which si not filled by user then we use `commit=False` and we must `exclude` that field from the form
> - `instance` is used to reference the query object which we are updating in our database

---
[⬆️ Go to Context](#context)

## Bootstrap In Django Form

- Django doesn’t automatically attach Bootstrap classes, so we have to apply it manually
- We can do this in two ways modify [forms.py](./form_app/forms.py) or using external package
- Using `widget`

  ```py
  class ProductForm(forms.ModelForm):
    class Meta:
      model=ProductModel
      fields='__all__'
      exclude=['product_total_amount']

      # using widgets and update individually
      widgets = {
          'product_name': forms.TextInput(attrs={'class': 'form-control'}),
          'product_price': forms.NumberInput(attrs={'class': 'form-control'}),
          'product_description': forms.Textarea(attrs={'class': 'form-control'}),
          'product_qty': forms.NumberInput(attrs={'class': 'form-control'}),

          # Choice field use form-select
          'product_cat': forms.Select(attrs={'class': 'form-select'}),

          # File input
          'product_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      }
  ```

- Override `__init__`

  ```py
  class ProductForm(forms.ModelForm):
    class Meta:
      model=ProductModel
      fields='__all__'
      exclude=['product_total_amount']

    # override __init__ and update using for loop
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)

      for field in self.fields.values():
          field.widget.attrs['class'] = 'form-control'
  ```

- Using external package [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/)
  - Install [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/)
  - Add this inside `INSTALLED_APPS` in [settings.py](./form_project/settings.py)

    ```py
    INSTALLED_APPS = (
        ...
        "crispy_forms",
        "crispy_bootstrap5",
    )
    ```

  - And at the end line of [settings.py](./form_project/settings.py) add this

    ```py
    # Bootstrap 5
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    CRISPY_TEMPLATE_PACK = "bootstrap5"
    ```

  - Now in each form HTML at the top add

    ```jinja
    {% extends 'master/base.html' %}
    {% load crispy_forms_tags %}

    {% block content %}
    <h1>Add product</h1>

    <form method="POST" enctype="multipart/form-data">
    {% csrf_token %}

      {{form_data | crispy }}

      <button type="submit" class="btn btn-primary">Add Product</button>
    </form>

    {% endblock content %}
    ```

    - Do the same in [product-edit.html](./form_app/templates/product-edit.html)

---
[⬆️ Go to Context](#context)

## Radio Select And Date Field In Django Form

- We already have category field in our model `product_cat` in [models.py](./form_app/models.py), we will make it radio select. And add a date field `product_date`
- In [forms.py](./form_app/forms.py) we have to manually make those changes using `widgets` for others field crispy will handle it auto

  ```py
  class ProductForm(forms.ModelForm):
    class Meta:
      model=ProductModel
      fields='__all__'
      exclude=['product_total_amount']

      widgets = {
          'product_cat': forms.RadioSelect(attrs={
            "class": "form-check-input",
          }),
          'product_date':forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
          })
      }
  ```

---
[⬆️ Go to Context](#context)
