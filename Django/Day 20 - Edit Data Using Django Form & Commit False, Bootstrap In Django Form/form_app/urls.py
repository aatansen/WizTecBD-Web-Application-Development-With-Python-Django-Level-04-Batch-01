from django.urls import path
from form_app.views import product_list,product_add,product_edit

urlpatterns = [
    path('',product_list,name='product_list'),
    path('product-add',product_add,name='product_add'),
    path('product-edit/<str:id>',product_edit,name='product_edit'),
]
