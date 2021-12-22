from django.shortcuts import render

# Create your views here.
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'frontend/home.html'
        )


class CourseView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'frontend/course.html'
        )
