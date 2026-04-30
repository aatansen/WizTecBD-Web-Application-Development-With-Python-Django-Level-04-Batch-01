from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# fields `username`, `full_name`, `email`, `password`, `confirm_password`
class CustomUserInfoModel(AbstractUser):
  full_name=models.CharField(max_length=100,null=True)

  def __str__(self):
    return f'{self.full_name}'

# - `title`, `description`, `status`(`Pending`, `InProgress`, `Completed`, `Canceled`), `due_date`, `created_at`, `updated_at`
class TaskModel(models.Model):
  title=models.CharField(max_length=100,null=True)
  description=models.TextField(null=True)

  STATUS=[
    ('Pending','Pending'),
    ('InProgress','InProgress'),
    ('Completed','Completed'),
    ('Canceled','Canceled'),
  ]
  status=models.CharField(choices=STATUS,max_length=100,null=True)
  due_date=models.DateField(null=True)
  created_at=models.DateField(auto_now_add=True,null=True)
  updated_at=models.DateField(auto_now=True,null=True)
  created_by=models.ForeignKey(CustomUserInfoModel,on_delete=models.CASCADE,null=True)

  def __str__(self):
    return f'{self.title}'
