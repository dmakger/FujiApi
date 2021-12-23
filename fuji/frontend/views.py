from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View
from .models import Course, Author


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'frontend/home.html'
        )


class CourseView(View):
    def get(self, request, *args, **kwargs):
        courses = list()
        for course in Course.objects.all():
            course.duration_in_minutes = self.get_duration(course.duration_in_minutes)
            courses.append(course)

        return render(request, 'frontend/course.html', context={
            'courses': courses
        })

    def get_duration(self, minutes):
        hours = round(minutes / 60, 1)
        if hours % 1 == 0:
            hours = int(hours)
        return f"{hours} ч"

# # class MainView(View):
# #     def get(self, request, *args, **kwargs):
# #         tests = Test.objects.all()
# #         return render(request, 'moon_test_app/home.html', context={
# #             'tests': tests
# #         })
