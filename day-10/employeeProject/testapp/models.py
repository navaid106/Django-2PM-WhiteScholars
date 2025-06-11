from django.db import models

class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=40)
    dob = models.DateField()
    salary = models.FloatField()
    designation = models.CharField(max_length=60)
    email = models.EmailField()

