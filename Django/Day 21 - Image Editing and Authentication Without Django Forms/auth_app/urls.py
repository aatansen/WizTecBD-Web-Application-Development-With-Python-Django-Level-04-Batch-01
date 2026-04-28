from django.urls import path
from auth_app.views import (
  student_list,
  student_add,
  student_edit,
  register_page,
  login_page,
  signout,
)

urlpatterns = [
  path('student-list/',student_list,name='student_list'),
  path('student-add/',student_add,name='student_add'),
  path('student-edit/<str:id>',student_edit,name='student_edit'),

  # authenticate
  path('',register_page,name='register_page'),
  path('login-page/',login_page,name='login_page'),
  path('signout/',signout,name='signout'),
]
