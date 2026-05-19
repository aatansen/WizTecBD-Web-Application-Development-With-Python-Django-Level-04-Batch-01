from django.urls import path
from api_app.views import *

urlpatterns = [
  # path('student-list/',student_list,name='student_list'),
  # path('student-add/',student_add,name='student_add'),

  # view all and add
  path('student/',student,name='student'),

  # individual view, update, delete
  path('student-details/<str:id>',student_details,name='student_details'),

]
