from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def admin(request):
    return render(request,'admin.html')

def Student(request):
    return render(request,'Student.html')

def assignDepartment(request):
    return render(request,'assignDepartment.html')

def viewStudent(request):
    return render(request,'viewStudent.html')

def browseCourse(request):
    return render(request,'browseCourse.html')

def viewID(request):
    return render(request,'viewID.html')

def viewGrades(request):
    return render(request,'viewGrades.html')

def viewSchedule(request):
    return render(request,'viewSchedule.html')





