from django.shortcuts import render,redirect
from school_app.models import studentModel

# Create your views here.
def student_list(request):
  student_data=studentModel.objects.all()

  context={
    'student_data':student_data,
  }

  return render(request,'student-list.html',context=context)

def add_student(request):
  if request.method=="POST":
    name = request.POST.get('name')
    age = request.POST.get('age')
    roll_no = request.POST.get('roll_no')

    studentModel.objects.create(
      name=name,
      age=age,
      roll_no=roll_no
    )
    return redirect('student_list')
  return render(request,'add-student.html')