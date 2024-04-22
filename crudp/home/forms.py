from django import forms
from.models import user

class students (forms.ModelForm):
    class meta:
        model = user
        fields = ['name','email','password']

