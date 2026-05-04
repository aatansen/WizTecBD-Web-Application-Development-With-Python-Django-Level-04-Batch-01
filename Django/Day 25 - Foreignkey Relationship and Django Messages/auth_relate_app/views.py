from django.shortcuts import render,redirect,get_object_or_404
from auth_relate_app.models import CustomUserModel,ProfileModel, ProductModel
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from auth_relate_app.forms import ProfileForm, ProductForm
from django.contrib import messages
from decimal import Decimal

# Create your views here.
def home_page(request):
    return render(request,'home-page.html')

@login_required
def profile_page(request):

    return render(request,'profile-page.html')

@login_required
def profile_update(request):
    current_user=request.user
    # model_data=get_object_or_404(ProfileModel,user=current_user)

    try:
        model_data=current_user.user_profile
    except:
        model_data=None

    # to update data in database
    form_data=ProfileForm(request.POST,request.FILES,instance=model_data)
    if form_data.is_valid():
        data=form_data.save(commit=False)
        data.user=current_user
        data.save()
        return redirect('profile_page')

    # to show the user model data in the form
    form_data=ProfileForm(instance=model_data)
    context={
        'form_title':'Profile Update',
        'form_btn':'Update',
        'form_data':form_data
    }
    return render(request,'master/base-form.html',context)

def register_page(request):
    if request.method=='POST':
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        c_password=request.POST.get('c_password')
        user_type = request.POST.get('user_type')

        if password==c_password:
            CustomUserModel.objects.create_user(
                full_name=full_name,
                username=username,
                email=email,
                password=password,
                user_type=user_type,
            )
            messages.success(request, 'Account created.')
            return redirect('login_page')
        else:
            messages.error(request, 'Password doesnot match.')
            return redirect('register_page')

    return render(request,'register-page.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
    
        user=authenticate(
            request,
            username=username,
            password=password
        )
        if user:
            login(request,user)
            
            return redirect('home_page')
    
    return render(request,'login-page.html')

@login_required
def signout(request):
  logout(request)
  return redirect('login_page')

#-----------Product
@login_required
def product_list(request):
    current_user = request.user

    if current_user.user_type == 'buyer':
        product_data = ProductModel.objects.all()
    else:
        product_data = ProductModel.objects.filter(created_by=request.user)
    context = {
        'product_data': product_data
    }
    return render(request, 'product-list.html',context)

@login_required
def add_product(request):
    if request.method == 'POST':
        form_data = ProductForm(request.POST)
        if form_data.is_valid():
            form_data = form_data.save(commit=False)
            form_data.created_by = request.user
            form_data.total_amount = form_data.price * Decimal(form_data.qty)
            form_data.save()
            messages.success(request, 'Product Created.')
            return redirect('product_list')
    form_data = ProductForm()
    context = {
        'form_data': form_data,
        'form_title': 'Add Product Info',
        'form_btn': 'Add Product',
    }
    
    return render(request, 'master/base-form.html',context)

@login_required
def update_product(request, id):
    try:
        product_data = ProductModel.objects.get(id=id)
    except ProductModel.DoesNotExist:
        product_data = None
    
    if request.method == 'POST':
        form_data = ProductForm(request.POST, instance=product_data)
        if form_data.is_valid():
            form_data = form_data.save(commit=False)
            form_data.created_by = request.user
            form_data.total_amount = form_data.price * Decimal(form_data.qty)
            form_data.save()
            messages.success(request,'Product Update Successfully.')
            return redirect('product_list')
        
    form_data = ProductForm(instance=product_data)
    context = {
        'form_data': form_data,
        'form_title': 'Update Product Info',
        'form_btn': 'Update Product',
    }
    return render(request, 'master/base-form.html',context)

