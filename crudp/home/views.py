from django.shortcuts import render,redirect
from.models import student
from django.contrib import messages
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
        messages.info(request,"Data Inserted Successfully")
    return redirect("/")

def updateData(request,id):
     if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        edit=student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

     d = student.objects.get(id=id)
     context={"d":d}
     return render(request,"edit.html",context)

def deleteData(request,id):
    d = student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")
    return redirect("/")
    
    return render(request,"delete.html",context)