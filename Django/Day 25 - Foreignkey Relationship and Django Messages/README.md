# Context

- [Context](#context)
  - [Foreignkey Relationship](#foreignkey-relationship)
  - [Django Messages](#django-messages)

## Foreignkey Relationship

- Create project
- Create App
- Add app to the project's [settings.py](./auth_relate_project/settings.py)
- Now Create model in [models.py](./auth_relate_app/models.py)

  ```py
  from django.db import models
  from django.contrib.auth.models import AbstractUser

  # Create your models here.

  class CustomUserModel(AbstractUser):
      USER_TYPES = [
          ('seller', 'Seller'),
          ('buyer', 'Buyer'),
      ]
      full_name = models.CharField(max_length=100, null=True)
      user_type = models.CharField(max_length=20, choices=USER_TYPES, null=True)

      def __str__(self):
          return f'{self.username}'


  class ProfileModel(models.Model):
      user = models.OneToOneField(
          CustomUserModel,
          on_delete=models.CASCADE,
          related_name='user_profile',
          null=True
      )
      address = models.TextField(null=True)
      dob = models.DateField(null=True)
      image = models.ImageField(upload_to='profile_img', null=True)

      def __str__(self):
          return f'{self.user}'


  class ProductModel(models.Model):
      name = models.CharField(max_length=200, null=True)
      description = models.TextField(null=True)
      price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
      qty = models.FloatField(null=True)
      total_amount = models.DecimalField(
          max_digits=10, decimal_places=2, null=True)
      created_by = models.ForeignKey(
          CustomUserModel,
          on_delete=models.CASCADE,
          null=True,
          related_name='user_product'
      )
      created_at = models.DateTimeField(auto_now_add=True, null=True)
      updated_at = models.DateTimeField(auto_now=True, null=True)

      def __str__(self):
          return f'{self.name}'
  ```

  - `CustomUserModel` is our auth model for user authentication and storing user data
  - `ProfileModel` is the extends of `CustomUserModel` where we made *one-to-one relationship* cause one user can have only one profile
  - `ProductModel` is created to show the `foreign key relationship` where it makes relationship with `CustomUserModel` and it is *one-to-many relationship*
  - Make sure to add a variable `AUTH_USER_MODEL` and store `app_name.custom_user_model_name` in [settings.py](./auth_relate_project/settings.py)

    ```py
    # auth model
    AUTH_USER_MODEL='auth_relate_app.CustomUserModel'
    ```

- Register all models in [admin.py](./auth_relate_app/admin.py)
- Create [forms.py](./auth_relate_app/forms.py) where we will create forms for `ProfileModel` and `ProductModel`

  ```py
  from django import forms
  from auth_relate_app.models import ProfileModel, ProductModel

  class ProfileForm(forms.ModelForm):
      class Meta:
          model=ProfileModel
          fields='__all__'
          exclude=['user']
          widgets={
              'dob':forms.DateInput(attrs={
                  'type':'date'
              })
          }

  class ProductForm(forms.ModelForm):
      class Meta:
          model = ProductModel
          fields = '__all__'
          exclude = ['total_amount','created_by']
  ```

  - Excluded fields must be handle in backend

- Run migration commands (both app and project level)
- Create `superuser`
- Create templates

  ```txt
  📁 templates
  ├── 📁 master
  │   ├── 🌐 base-form.html
  │   ├── 🌐 base.html
  │   ├── 🌐 messages.html
  │   └── 🌐 nav.html
  ├── 🌐 home-page.html
  ├── 🌐 login.html
  ├── 🌐 product-list.html
  ├── 🌐 profile-page.html
  └── 🌐 register-page.html
  ```

- Create [views](./auth_relate_app/views.py) and [urls](./auth_relate_app/urls.py) for each of those templates
  - In product list page we have shown it based on user type

    ```py
    @login_required
    def product_list(request):
        current_user = request.user

        if current_user.user_type == 'buyer':
            product_data = ProductModel.objects.all()
        else:
            product_data = ProductModel.objects.filter(created_by=request.user)
        context = {
            'product_data': product_data
        }
        return render(request, 'product-list.html',context)
    ```

- Include app `urls` to project `urls`
- In our model we have image field so `pillow` package and media setup is required in [settings.py](./auth_relate_project/settings.py) and project [urls.py](./auth_relate_project/urls.py)

  `urls.py`

  ```py
  ...
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
      ...
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```

  `settings.py`

  ```py
  # media settings
  MEDIA_URL='media/'
  MEDIA_ROOT=BASE_DIR/'media/'
  ```

## Django Messages

- To show message to user when in frontend we use `django messages`

  ```py
  from django.contrib import messages
  ```

- In each operation where we used `redirect` before that line we will use `messages` and the message will show in the redirect page

  ```py
  def register_page(request):
      if request.method=='POST':
          ...
          if password==c_password:
              ...
              messages.success(request, 'Account created.')
              return redirect('login_page')
          else:
              messages.error(request, 'Password doesnot match.')
              return redirect('register_page')

      return render(request,'register-page.html')
  ```

- Now Create an HTML page in master [messages.html](./auth_relate_app/templates/master/messages.html)

  ```jinja
  {% if messages %}

  {% for i in messages %}
      <div class="alert alert-primary" role="alert">
          {{i}}
      </div>
  {% endfor %}

  {% endif %}
  ```

- In the page where we are redirecting we will include this [messages.html](./auth_relate_app/templates/master/messages.html)

  ```jinja
  {% include 'master/messages.html' %}
  ```

> [!IMPORTANT]
>
> - When you are making relationship with other model > ask yourself question it will provide answer to which type of relation it can be. e.g.:A user(buyer/seller) can buy/add many product (`ForeignKey` - one-to-many). Now a user can have only one profile (`OneToOneField` - one-to-one)
> - If you use Decimal in model fields, make sure to convert other number field to it using `from decimal import Decimal`

---
[⬆️ Go to Context](#context)
