from django import forms
from form_app.models import ProductModel

class ProductForm(forms.ModelForm):
  class Meta:
    model=ProductModel
    fields='__all__'
    exclude=['product_total_amount']

  # override __init__ and update using for loop
  # def __init__(self, *args, **kwargs):
  #   super().__init__(*args, **kwargs)

  #   for field in self.fields.values():
  #       field.widget.attrs['class'] = 'form-control'



    # using widgets and update individually
    # widgets = {
    #     'product_name': forms.TextInput(attrs={'class': 'form-control'}),
    #     'product_price': forms.NumberInput(attrs={'class': 'form-control'}),
    #     'product_description': forms.Textarea(attrs={'class': 'form-control'}),
    #     'product_qty': forms.NumberInput(attrs={'class': 'form-control'}),

    #     # Choice field → use form-select
    #     'product_cat': forms.Select(attrs={'class': 'form-select'}),

    #     # File input
    #     'product_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
    # }