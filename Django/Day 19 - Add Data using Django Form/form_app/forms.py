from django import forms
from form_app.models import ProductModel

class ProductForm(forms.ModelForm):
  class Meta:
    model=ProductModel
    fields='__all__'
