from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def portfolio_view(request):
    # return HttpResponse('Portfolio Page.')

    return render(request,'testapp/index.html')
