from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    s='<h1>Welcome to Django Project</h1>'
    return HttpResponse(s)

def mobile(request):
    s='<h1 style="background-color:red; font-size:40px;">Welcome to mobile page</h1>'
    return HttpResponse(s)