from django.urls import path
from auth_relate_app.views import (
    home_page,
    profile_page,
    register_page,
    login_page,
    signout,
    profile_update,

    product_list,
    add_product,
    update_product
)

urlpatterns = [
    path('',register_page,name='register_page'),
    path('home-page/',home_page,name='home_page'),

    path('login-page/',login_page,name='login_page'),
    path('signout/',signout,name='signout'),

    path('profile-page/',profile_page,name='profile_page'),
    path('profile-update/',profile_update,name='profile_update'),

    path('product-list/',product_list, name='product_list'),
    path('add-product/',add_product,name='add_product'),
    path('update-product/<int:id>/',update_product,name='update_product')
]