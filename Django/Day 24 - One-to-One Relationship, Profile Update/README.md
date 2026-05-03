# Context

- [Context](#context)
  - [One-to-One Relationship](#one-to-one-relationship)
  - [Profile Update](#profile-update)

## One-to-One Relationship

- In our existing project for example To-Do Application on [Day 22](../Day%2022%20-%20Demonstration-02(To-Do%20List%20Application)/) we will add One-to-One relationship
- First let's update model

  ```py
  class CustomUserInfoModel(AbstractUser):
    full_name=models.CharField(max_length=100,null=True)

    def __str__(self):
      return f'{self.full_name}'

  class ProfileModel(models.Model):
    user=models.OneToOneField(CustomUserInfoModel,on_delete=models.CASCADE,null=True,related_name='user_profile')
    address=models.TextField(null=True)
    contact=models.TextField(max_length=100,null=True)
    image=models.ImageField(upload_to='profile-img',null=True)

    def __str__(self):
      return f'{self.user}'
  ```

  - In here we make a one-to-one relationship in `ProfileModel` with `CustomUserInfoModel` and the logic is one user (`CustomUserInfoModel`) can have only one profile(`ProfileModel`)
  - in `image` field we used to give `upload_to='media/profile-img'`, but we can mention `MEDIA_URL` and `MEDIA_ROOT` in [settings.py](./todo_project/settings.py) then we won't need to add `media/` in the path only the folder name `upload_to='profile-img'`

    ```py
    # media setting
    MEDIA_URL='media/'
    MEDIA_ROOT=BASE_DIR/'media/'
    ```

  - As we are using image field so we need to configure project [urls.py](./todo_project/urls.py) and install pillow

    ```py
    ...
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    ```

- Register it in [admin.py](./tasks/admin.py)
- Run App level migration commands
- Now we will create an HTML page [profile-page.html](./tasks/templates/profile-page.html) view function to render it

  ```py
  # profile
  def profile_page(request):
    return render(request,'profile-page.html')
  ```

- Add URL path in [urls.py](./tasks/urls.py)
- Add the URL name in [nav.html](./tasks/templates/master/nav.html)

- In [profile-page.html](./tasks/templates/profile-page.html) we can access values without sending any context cause we have `request.user` and `related_name` in our model

  ```jinja
  {% extends 'master/base.html' %}

  {% block content %}

  <h1>Profile Page</h1>
  <p>Full Name: {{request.user.full_name}}</p>
  <p>Address: {{request.user.user_profile.address}}</p>
  <p>Contact: {{request.user.user_profile.contact}}</p>
  <p>DoB: {{request.user.user_profile.dob}}</p>

  <a href="" class="btn btn-primary">Update Profile</a>

  {% endblock content %}
  ```

  - We access `CustomUserInfoModel` data using `request.user` and `ProfileModel` data using `{{request.user.user_profile.address}}`
  - Added a `Update Profile` button to update the profile data

---
[⬆️ Go to Context](#context)

## Profile Update

- As it is going to show the form after clicking so we will make profile form in [forms.py](./tasks/forms.py)

  ```py
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
  ```

  - We exclude `user` which is the one-to-one relation field cause user in the frontend won't provide it, we have to assign it in the backend
  - In `dob` field of `ProfileModel` is date field which we need to mention the type to format it properly date field in the HTML form page
  - For others field we are using [crispy-bootstrap5](https://pypi.org/project/crispy-bootstrap5/)

- Now we will create a function in [views.py](./tasks/views.py)

  ```py
  @login_required
  def profile_update(request):
    current_user=request.user
    try:
      # using get query
      profile_data=get_object_or_404(ProfileModel,user=current_user)

      # using related name
      # profile_data=current_user.user_profile
    except:
      profile_data=None

    # to update the data in database
    if request.method=="POST":
      form_data=ProfileForm(request.POST,request.FILES,instance=profile_data)
      if form_data.is_valid():
        data=form_data.save(commit=False)
        data.user=current_user
        data.save()
        return redirect('profile_page')

    # to show the current model data and form
    form_data=ProfileForm(instance=profile_data)
    context={
      'form_data':form_data,
      'form_title':'Update Profile',
      'form_btn':'Update'
    }

    return render(request,'master/base-form.html',context=context)
  ```

  - In here we are updating profile data using `request.user`, if we remember we used to use `id` where we are supposed to `update`,`delete`,`view data`, but now we are using `request.user` cause when a user logged in it actually have all the model data access so we can easily access those data
  - There is `try` and `except` block which is used to prevent data not found in the model, it is advised to use it when we use `get` / `get_object_or_404` query to get the data, so the missing data can be updated
  - In the `try` block we can get data in *two ways* one is using `current_user` and `get_object_or_404` / `get` another is `current_user.user_profile` where `current_user` is `request.user` and `user_profile` is the `related_name` in the model `ProfileModel` we mentioned
  - `data.user=current_user` is the user which we excluded in the `ProfileForm`

- Add URL path in [urls.py](./tasks/urls.py)
- Add the URL name in [profile-page.html](./tasks/templates/profile-page.html) update profile button `a tag`

> [!IMPORTANT]
>
> - Defining `MEDIA_URL` and `MEDIA_ROOT` in the `settings.py` is very important when deploying
> - Make sure you used `related_name` in the relation field, so data can be access easily. It is the name used to access a model’s related objects from the reverse (accessing related data from the opposite) side of a Django relationship.
> - We access our auth user data using `{{request.user}}`, and now we can access the other model too where auth model is related with one-to-one relation using its `related_name` which is `{{request.user.user_profile.address}}`
> - Make sure to use `try`, `except` to handle error specially when getting data could be missing

---
[⬆️ Go to Context](#context)
