from django.shortcuts import render
from.forms import students
# Create your views here.

def index(request):
    return render(request,"index.html")

def insertData(request):
    return render(request,"index.html")