from django.shortcuts import render

# Create your views here.

def portfolio_view(request):
    # rendering html page(template) as response
    return render(request,'testapp/index.html')

def about_view(request):
    return render(request,'testapp/about.html')