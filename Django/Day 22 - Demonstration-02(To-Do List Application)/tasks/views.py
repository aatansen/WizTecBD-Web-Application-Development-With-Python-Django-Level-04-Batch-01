from django.template.context_processors import request
# django imports
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# my app forms and models
from tasks.models import CustomUserInfoModel,TaskModel
from tasks.forms import TaskForm

# Authentication
def register_page(request):
  if request.method=="POST":
    username=request.POST.get('username')
    full_name=request.POST.get('full_name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    c_password=request.POST.get('c_password')

    if password==c_password:
      CustomUserInfoModel.objects.create_user(
        username=username,
        full_name=full_name,
        password=password,
        email=email
      )
      return redirect('login_page')

  return render(request,'register-page.html')

def login_page(request):
  if request.method=="POST":
    username=request.POST.get('username')
    password=request.POST.get('password')

    user = authenticate(
      request,
      username=username,
      password=password,
    )
    if user:
      login(request,user)
      return redirect('home_page')
  return render(request,'login-page.html')

def signout(request):
  logout(request)
  return redirect('login_page')

# home
def home_page(request):
  return render(request,'home-page.html')

# task
@login_required
def task_list(request):
  task_data=TaskModel.objects.filter(created_by=request.user)

  context={
    'task_data':task_data
  }
  return render(request,'task-list.html',context=context)

@login_required
def task_add(request):

  # to save form data to database
  if request.method=="POST":
    form_data=TaskForm(request.POST)
    if form_data.is_valid():
      data=form_data.save(commit=False)
      data.created_by=request.user
      data.save()
      return redirect('task_list')

  # to show the form
  form_data=TaskForm()
  context={
    'form_data':form_data,
    'form_title':'Add Task Page',
    'form_btn':'Add Task',
  }
  return render(request,'master/base-form.html',context)

@login_required
def task_edit(request,id):
  task_data=get_object_or_404(TaskModel,id=id)
  # to save form data to database
  if request.method=="POST":
    form_data=TaskForm(request.POST,instance=task_data)
    if form_data.is_valid():
      data=form_data.save(commit=False)
      data.created_by=request.user
      data.save()
      return redirect('task_list')

  # to show the form
  form_data=TaskForm(instance=task_data)
  context={
    'form_data':form_data,
    'form_title':'Update Task Page',
    'form_btn':'Update Task',
  }
  return render(request,'master/base-form.html',context)

def task_detail(request,id):
  task_data=get_object_or_404(TaskModel,id=id)

  context={
    'task_data':task_data,
  }
  return render(request,'task-detail.html',context=context)

def task_delete(request,id):
  task_data=get_object_or_404(TaskModel,id=id)
  task_data.delete()
  return redirect('task_list')
