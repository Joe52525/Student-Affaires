

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'JIMM/index.html')

def admin(request):
    return render(request,'JIMM/admin.html')

def Student(request):
    return render(request,'JIMM/Student.html')

def assignDepartment(request):
    return render(request,'JIMM/assignDepartment.html')

def viewStudent(request):
    return render(request,'JIMM/viewStudent.html')

def browseCourse(request):
    return render(request,'JIMM/browseCourse.html')

def viewID(request):
    return render(request,'JIMM/viewID.html')

def viewGrades(request):
    return render(request,'JIMM/viewGrades.html')

def viewSchedule(request):
    return render(request,'JIMM/viewSchedule.html')

def RegisterCourse(request):
    return render(request,'JIMM/RegisterCourse.html')

def academicCalendar(request):
    return render(request,'JIMM/academicCalendar.html')

def newsAnnouncements(request):
    return render(request,'JIMM/newsAnnouncements.html')

def courseManagement(request):
    return render(request,'JIMM/courseManagement.html')

def courseAssessment(request):
    return render(request,'JIMM/courseAssessment.html')

def instructorAssignment(request):
    return render(request,'JIMM/instructorAssignment.html')

def courseCatalog(request):
    return render(request,'JIMM/courseCatalog.html')

def courseEvaluation(request):
    return render(request,'JIMM/courseEvaluation.html')

def courseReport(request):
    return render(request,'JIMM/courseReport.html')

from django.shortcuts import render
from .models import Instructor, Course  # Make sure to import your models

def assign_instructor_view(request):
    instructors = Instructor.objects.all()
    courses = Course.objects.all()
    return render(request, 'instructorAssignment.html', {'instructors': instructors, 'courses': courses})






