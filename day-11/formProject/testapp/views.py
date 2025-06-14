from django.shortcuts import render
from testapp.forms import studentForm

def student_view(request):
	# create object of form class
	form = studentForm() #object created
	return render(request, 'testapp/student.html',{'form':form})

