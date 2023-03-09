from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Semester, Section, Course, Instructor, Student, Registration, Period, Year
from django.urls import reverse
from django.urls import reverse
from django.core.exceptions import ValidationError

# Test view templates
class InstructorTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        cls.instructor = Instructor.objects.create(first_name='Hong', last_name='Lang')

    #test the model
    def test_instructor_name(self):
        self.assertEqual(f'{self.instructor.first_name}', 'Hong')
        self.assertEqual(f'{self.instructor.last_name}', 'Lang')
        #test the string representation
        self.assertEqual(str(self.instructor), 'Hong, Lang')
    #test the unique entry
    def test_if_instructor_name_unique(self):
        unique_test = Instructor.objects.create(first_name='Hong', last_name='Lang')
        with self.assertRaisesMessage(
            ValidationError,
            'Instructor with this Instructor name already exists.',
        ):
            unique_test.full_clean()

    #test the content ordering
    def test_ordering(self):
        Instructor.objects.create(first_name='Yaman', last_name='Yu')
        instructor_list = Instructor.objects.all()
        self.assertEqual(instructor_list[0].first_name, 'Hong')

    #test the view
    def test_instructor_view_with_instructors(self):
        response = self.client.get(reverse('instructor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/instructor_list.html')
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertContains(response, 'Hong, Lang')
        self.assertContains(response, 'Yaman, Yu')


    def test_instructor_view_without_instructors(self):
        Instructor.objects.all().delete()
        response = self.client.get(reverse('instructor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courseinfo/instructor_list.html')
        self.assertTemplateUsed(response, 'courseinfo/base.html')
        self.assertContains(response, 'There are no instructors available.')


class SectionTest(TestCase):
    def setUp(cls):
        cls.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        year = Year.objects.create(year='2021')
        period = Period.objects.create(period_sequence=1, period_name='Spring')
        semester = Semester.objects.create(year=year, period=period)
        course = Course.objects.create(course_number=1, course_name='IS439')
        cls.section = Section.objects.create(section_name='Section A', semester=semester, course=course)


