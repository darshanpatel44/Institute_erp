from django.urls import include,path
from . import views

urlpatterns=[
    path("home/",views.faculty_home),
    path("attendance/",views.faculty_attendance),
    path("attendance_update/",views.faculty_attendance_update),
    path("marks/",views.faculty_marks),
    path("marks_update/",views.faculty_marks_update),
    path("course/",views.faculty_course),
    # path("timetable/",views.student_timetable),
    
]