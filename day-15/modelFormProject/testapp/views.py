from django.shortcuts import render
from .forms import StudentForm
from testapp.models import Student


def home_view(request):
    return render(request,'testapp/home.html')


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


# Write logic to fetch data from database table

def fetchData_view(request):
    student_list = Student.objects.all() #fetch data from database table
    dict = {'student_list':student_list} #dictionary----> key:value

    return render(request,'testapp/displayStudent.html',dict) #sending data on displayStudent.html file

