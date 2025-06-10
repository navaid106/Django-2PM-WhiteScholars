from django.db import models


class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=40)
    course = models.CharField(max_length=60)
    email = models.EmailField()