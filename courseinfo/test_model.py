from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year
from django.urls import reverse