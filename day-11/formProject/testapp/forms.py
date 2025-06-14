from django import forms

class studentForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    marks = forms.FloatField()