from django.shortcuts import render

def home_page(request):
  info = {
    "name": "Tansen",
    "address": "Dhaka"
  }
  return render(request, 'home.html', context=info)

def about_page(request):
  return render(request,'about.html')