from django.contrib import admin
from auth_relate_app.models import (
  CustomUserModel,
  ProfileModel,
  ProductModel
)

# Register your models here.
admin.site.register([
  CustomUserModel,
  ProfileModel,
  ProductModel,
])