from django.shortcuts import render
from testapp.forms import FeedbackForm
# Create your views here.

def feedback_view(request):
    
    # if request.method == 'POST':
        
    # 

    form = FeedbackForm() #creating object
    dict={'form':form}
    return render(request,'testapp/feedback.html',dict)