from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import datetime

def time_page_view(request):
    # creating object of datetime
    date = datetime.datetime.now()
    msg = f'The current server time is: '

    msg+= ' ---> '+str(date)


    return HttpResponse(msg)
