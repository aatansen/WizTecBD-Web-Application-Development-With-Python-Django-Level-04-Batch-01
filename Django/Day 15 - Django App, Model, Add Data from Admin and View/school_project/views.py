from django.shortcuts import render
from school_app.models import TeacherModel

def home_page(request):
  return render(request,'home.html')

def teacher_page(request):

  teacher_data=TeacherModel.objects.all()

  context={
    'teacher_data':teacher_data
  }

  return render(request,'teacher.html',context=context)
