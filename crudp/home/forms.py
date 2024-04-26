from django import forms
from.models import student

class students (forms.ModelForm):
    class meta:
        model = student
        fields = ['name','email','age','gender']

