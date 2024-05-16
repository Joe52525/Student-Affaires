
from django.urls import path, include
from . import views
urlpatterns = [

    path('',views.index,name='index'),
    path('admin',views.admin,name='admin'),
    path('Student',views.Student,name='Student'),
    path('assignDepartment',views.assignDepartment,name='assignDepartment'),
    path('viewStudent',views.viewStudent,name='viewStudent'),
    path('browseCourse',views.browseCourse,name='browseCourse'),
    path('viewID',views.viewID,name='viewID'),
    path('viewGrades',views.viewGrades,name='viewGrades'),
    path('viewSchedule',views.viewSchedule,name='viewSchedule'),
    path('RegisterCourse',views.RegisterCourse,name='RegisterCourse'),
    path('academicCalendar',views.academicCalendar,name='academicCalendar'),
    path('newsAnnouncements',views.newsAnnouncements,name='newsAnnouncements'),
    path('courseManagement',views.courseManagement,name='courseManagement'),
    path('courseAssessment',views.courseAssessment,name='courseAssessment'),
    path('instructorAssignment',views.instructorAssignment,name='instructorAssignment'),
    path('courseCatalog',views.courseCatalog,name='courseCatalog'),
    path('courseEvaluation',views.courseEvaluation,name='courseEvaluation'),
    path('courseReport',views.courseReport,name='courseReport'),
]