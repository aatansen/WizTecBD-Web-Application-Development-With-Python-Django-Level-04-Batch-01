from django.http import HttpResponse

def home_page(request):
  msg="Hello World"
  return HttpResponse(msg)