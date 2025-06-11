from django.shortcuts import render
from testapp.models import Employee

def employee_view(request):
    emp_list = Employee.objects.all() #fetching employee data from table.
    dict = {'emp_list':emp_list}
    return render(request,'testapp/employee.html',dict)
