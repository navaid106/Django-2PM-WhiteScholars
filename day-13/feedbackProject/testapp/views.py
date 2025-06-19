from django.shortcuts import render
from testapp.forms import FeedbackForm
# Create your views here.

def feedback_view(request):
    
    data={}
    # This code will execute when you'll submit the form
    if request.method == 'POST':
        # object for POST
        form = FeedbackForm(request.POST)

        if form.is_valid(): #True | False
            # This data we're priting on console
            print(f'Name---->{form.cleaned_data['name']}')
            print(f'Rollno---->{form.cleaned_data['rollno']}')
            print(f'Email---->{form.cleaned_data['email']}')
            print(f'Feedback---->{form.cleaned_data['feedback']}')

            data = {
                # key:value --> pair
                'name':form.cleaned_data['name'],
                'rollno':form.cleaned_data['rollno'],
                'email':form.cleaned_data['email'],
                'feedback':form.cleaned_data['feedback'],
            }
            

    
    # object for GET
    form = FeedbackForm() #creating object
    dict={'form':form,'data':data}
    return render(request,'testapp/feedback.html',dict)


def submitted_view(request):
     # object for GET
    form = FeedbackForm() #creating object
    data = {}

      # This code will execute when you'll submit the form
    if request.method == 'POST':
        # object for POST
        form = FeedbackForm(request.POST)

        if form.is_valid(): #True | False
            # print(f'Name---->{form.cleaned_data['name']}')
            # print(f'Rollno---->{form.cleaned_data['rollno']}')
            # print(f'Email---->{form.cleaned_data['email']}')
            # print(f'Feedback---->{form.cleaned_data['feedback']}')

            data = {
                # key:value --> pair
                'name':form.cleaned_data['name'],
                'rollno':form.cleaned_data['rollno'],
                'email':form.cleaned_data['email'],
                'feedback':form.cleaned_data['feedback'],
            }

          
            
    dict={
        'form':form,
        'data':data,
        
        }
    return render(request,'testapp/formData.html',dict)




