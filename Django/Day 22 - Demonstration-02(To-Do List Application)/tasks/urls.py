from django.urls import path
from tasks.views import (
  register_page,
  login_page,
  signout,
  home_page,
  task_list,
  task_add,
  task_edit,
  task_detail,
  task_delete,
)

urlpatterns = [
  # authentication
  path('',register_page,name='register_page'),
  path('login-page/',login_page,name='login_page'),
  path('signout/',signout,name='signout'),

  # home
  path('home-page/',home_page,name='home_page'),


  # task
  path('task-list/',task_list,name='task_list'),
  path('task-add/',task_add,name='task_add'),
  path('task-edit/<str:id>/',task_edit,name='task_edit'),
  path('task-detail/<str:id>/',task_detail,name='task_detail'),
  path('task-delete/<str:id>/',task_delete,name='task_delete'),
]
