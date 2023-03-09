from django.shortcuts import render

from courseinfo.models import Instructor
from courseinfo.models import Section, Course, Semester, Student, Registration


# Create your views here.
def instructor_list_view(request):
    instructor_list = Instructor.objects.all()
    return render(request, 'courseinfo/instructor_list.html', {'instructor_list': instructor_list})


def section_list_view(request):
    section_list = Section.objects.all()
    return render(request, 'courseinfo/section_list.html', {'section_list': section_list})


def course_list_view(request):
    course_list = Course.objects.all()
    return render(request, 'courseinfo/course_list.html', {'course_list': course_list})


def semester_list_view(request):
    semester_list = Semester.objects.all()
    return render(request, 'courseinfo/semester_list.html', {'semester_list': semester_list})


def student_list_view(request):
    student_list = Student.objects.all()
    return render(request, 'courseinfo/student_list.html', {'student_list': student_list})


def registration_list_view(request):
    registration_list = Registration.objects.all()
    return render(request, 'courseinfo/registration_list.html', {'registration_list': registration_list})
