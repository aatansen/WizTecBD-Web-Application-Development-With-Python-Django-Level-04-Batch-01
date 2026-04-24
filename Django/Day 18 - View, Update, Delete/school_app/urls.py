from django.urls import path
from school_app.views import student_list,add_student,view_student,delete_student,update_student

urlpatterns = [
    path('',student_list,name='student_list'),
    path('add-student/',add_student,name='add_student'),
    path('view-student/<str:id>/',view_student,name='view_student'),
    path('delete-student/<str:id>/',delete_student,name='delete_student'),
    path('update-student/<str:id>/',update_student,name='update_student'),
]
