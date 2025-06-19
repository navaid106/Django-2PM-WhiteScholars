from django.db import models

class Student(models.Model):
    name  = models.CharField(max_length=50)
    rollno = models.IntegerField()
    marks = models.FloatField()
    
