from django.shortcuts import render
from .forms import StudentForm

def student_view(request):

    # POST
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid(): #True
            form.save(commit=True) #saving data into database
            form = StudentForm() # reset the form data

    # GET
    else:
        form = StudentForm() # creating form object
        

    return render(request,'testapp/student.html',{'form':form})

