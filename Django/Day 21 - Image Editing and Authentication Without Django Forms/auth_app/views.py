from django.shortcuts import render,redirect
from auth_app.models import StudentModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def student_list(request):
  student_data=StudentModel.objects.all()
  context={
    'student_data':student_data
  }
  return render(request,'student-list.html',context=context)

@login_required
def student_add(request):
  if request.method=="POST":
    name=request.POST.get('name')
    profile_pic=request.FILES.get('profile_pic')

    StudentModel.objects.create(
      name=name,
      profile_pic=profile_pic
    )
    return redirect('student_list')

  return render(request,'student-add.html')

@login_required
def student_edit(request,id):
  student_data=StudentModel.objects.get(id=id)

  # Get data from html page form
  if request.method=="POST":
    name=request.POST.get('name')
    profile_pic=request.FILES.get('profile_pic')

    # update the data to database
    student_data.name=name
    if profile_pic:
      student_data.profile_pic=profile_pic
    student_data.save()
    return redirect('student_list')

    # we can do this but not recommended
    # if not profile_pic:
    #   profile_pic=student_data.profile_pic
    # StudentModel(
    #   id=id,
    #   name=name,
    #   profile_pic=profile_pic,
    # ).save()

  # to show current model data in value attribute
  context={
    'student_data':student_data
  }

  return render(request,'student-edit.html',context=context)


def register_page(request):
  if request.method=="POST":
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    c_password=request.POST.get('c_password')

    if password==c_password:
      User.objects.create_user(
        username=username,
        email=email,
        password=password
      )
      return redirect('login_page')

  return render(request,'register.html')

def login_page(request):
  if request.method=="POST":
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(
      request,
      username=username,
      password=password,
    )
    if user:
      login(request,user)
      return redirect('student_list')

  return render(request,'login-page.html')

def signout(request):
  logout(request)
  return redirect('login_page')
