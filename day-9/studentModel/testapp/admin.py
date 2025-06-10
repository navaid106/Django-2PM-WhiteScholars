from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','course','email']

admin.site.register(Student,StudentAdmin)
