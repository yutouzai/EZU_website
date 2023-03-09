from django.contrib import admin
from django.urls import path, include
from courseinfo.views import (
    instructor_list_view,
    section_list_view,
    course_list_view,
    semester_list_view,
    student_list_view,
    registration_list_view
)

path('instructor/', instructor_list_view, name='instructor'),
path('section/', section_list_view, name='section'),
path('course/', course_list_view, name='course'),
path('semester/', semester_list_view, name='semester'),
path('student/', student_list_view, name='student'),
path('registration/', registration_list_view, name='registration')