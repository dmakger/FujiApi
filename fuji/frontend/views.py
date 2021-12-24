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
            course.rating = self.get_rating(course.rating)
            courses.append(course)

        return render(request, 'frontend/course.html', context={
            'courses': courses
        })

    def get_duration(self, minutes):
        return f"{round(minutes / 60)} ч"

    def get_rating(self, rating):
        rating_int = int(rating)
        if rating_int == rating:
            return rating_int
        return rating

# # class MainView(View):
# #     def get(self, request, *args, **kwargs):
# #         tests = Test.objects.all()
# #         return render(request, 'moon_test_app/home.html', context={
# #             'tests': tests
# #         })
