from django.shortcuts import render
from.models import student
# Create your views here.

def index(request):
    data = student.objects.all()
    print(data)
    context={"data":data}
    print(context)
    return render(request,"index.html",context)

def insertData(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)
        query = student(name=name,email=email,age=age,gender=gender)
        query.save()
    return render(request,"index.html")

def updateData(request,id):
    data = student.objects.all()
    print(data)
    context={"data":data}
    
    return render(request,"update.html",context)

def deleteData(request,id):
    data = student.objects.all()
    print(data)
    context={"data":data}
   
    return render(request,"delete.html",context)