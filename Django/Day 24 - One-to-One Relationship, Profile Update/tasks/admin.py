from django.contrib import admin
from tasks.models import CustomUserInfoModel,TaskModel
# Register your models here.

admin.site.register(
  [
    CustomUserInfoModel,
    TaskModel,
  ]
)
