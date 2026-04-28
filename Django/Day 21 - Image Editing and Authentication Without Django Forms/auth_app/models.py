from django.db import models

# Create your models here.

class StudentModel(models.Model):
  name=models.CharField(max_length=100)
  profile_pic=models.ImageField(upload_to='media/profile_pic')

  def __str__(self):
    return f'{self.name}'