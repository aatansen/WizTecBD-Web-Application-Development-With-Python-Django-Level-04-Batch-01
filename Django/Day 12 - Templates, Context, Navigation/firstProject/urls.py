from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home'),
    path('about/',views.about_page,name='about'),
]
