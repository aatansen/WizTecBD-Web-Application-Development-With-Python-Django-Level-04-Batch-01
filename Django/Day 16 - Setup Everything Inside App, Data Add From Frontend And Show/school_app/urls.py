from django.urls import path
from school_app.views import student_list,add_student

urlpatterns = [
    path('',student_list,name='student_list'),
    path('add-student/',add_student,name='add_student'),
]
