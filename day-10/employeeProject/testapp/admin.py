from django.contrib import admin
from testapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['empid','name','dob','salary','designation','email']


admin.site.register(Employee,EmployeeAdmin)
