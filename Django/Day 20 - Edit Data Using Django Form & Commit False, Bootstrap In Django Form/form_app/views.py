from django.shortcuts import render,redirect
from form_app.models import ProductModel
from form_app.forms import ProductForm

# Create your views here.
def product_list(request):
  product_data=ProductModel.objects.all()
  context={
    'product_data':product_data
  }
  return render(request,'product-list.html',context=context)

def product_add(request):
  # to save the form data in database
  if request.method == 'POST':
    form_data=ProductForm(request.POST, request.FILES)
    if form_data.is_valid():
      form_data.save()
      return redirect('product_list')

  # to show the form in html page
  form_data=ProductForm()
  context={
    'form_data':form_data
  }
  return render(request,'product-add.html',context=context)

def product_edit(request,id):
  product_data=ProductModel.objects.get(id=id)

  # to update data in database
  if request.method == 'POST':
    form_data=ProductForm(request.POST,request.FILES,instance=product_data)
    if form_data.is_valid():
      data=form_data.save(commit=False)
      data.product_total_amount=data.product_price*data.product_qty
      data.save()
      return redirect('product_list')

  # to show the form in html page
  form_data=ProductForm(instance=product_data)
  context={
    'form_data':form_data
  }
  return render(request,'product-edit.html',context=context)