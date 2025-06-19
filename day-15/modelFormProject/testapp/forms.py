from django import forms
from testapp.models import Student

class StudentForm(forms.ModelForm):
    # create form input fields
    name  = forms.CharField()
    rollno = forms.IntegerField()
    marks = forms.FloatField()

    class Meta:
        model = Student #model class name
        fields = '__all__' # want to use all column of database table.
