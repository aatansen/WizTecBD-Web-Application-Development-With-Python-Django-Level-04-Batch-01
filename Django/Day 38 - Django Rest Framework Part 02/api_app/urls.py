from django.urls import path
from api_app.views import *

urlpatterns = [
  path('student-api/',student_api.as_view(), name='student_api'),
  path('student-detail-api/<str:pk>/',student_detail_api.as_view(), name='student_detail_api'),
]
