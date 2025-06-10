from django.shortcuts import render
from .models import Student

def student_view(request):
   
    students = Student.objects.all()  # select * from Student; (ORM)

    dict = {'students':students}

    return render(request, 'testapp/students.html',dict)
    