from django.shortcuts import render
from.forms import students
# Create your views here.

def add (request):
    form=students()
    if request.method == 'POST':
        fm=students(request.POST)
    return render(request,'add.html',{'forms':"fm"})