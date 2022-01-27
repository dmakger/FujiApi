from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect

# Create your views here.
from django.views import View
from .models import Course, CourseInfo
# from .models import Profile
from .forms import SignUpForm, SignInForm


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'frontend/home.html'
        )


class SignUpView(View):
    """Регистрация"""
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, "frontend/signup.html", context={
            'form': form
        })

    # def post(self, request, *args, **kwargs):
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user_form = form.save()
    #
    #         if user_form is not None:
    #             profile = Profile(
    #                 user=user_form,
    #                 name=request.POST['name'],
    #                 last_name=request.POST['last_name'],
    #                 avatar_url="https://i.ibb.co/Bf4KMdp/logo-person.jpg",
    #                 mail=request.POST['mail'],
    #                 about_me_text="Я чел",
    #             )
    #             profile.save()
    #             login(request, user_form)
    #             return HttpResponseRedirect('/')
    #     return render(request, 'frontend/signup.html', context={
    #         'form': form,
    #     })


class SignInView(View):
    """Вход"""
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, "frontend/signin.html", context={
            'form': form
        })

    # def post(self, request, *args, **kwargs):
    #     form = SignInForm(request.POST)
    #     if form.is_valid():
    #         username = request.POST['username']
    #         password = request.POST['password']
    #         user = authenticate(request, username=username, password=password)
    #
    #         if user is not None:
    #             login(request, user)
    #             return HttpResponseRedirect('/')
    #     return render(request, "frontend/signin.html", context={
    #         'form': form
    #     })


class CourseView(View):
    def get(self, request, *args, **kwargs):
        courses = list()
        for course in Course.objects.all():
            course.duration_in_minutes = self.get_duration(course.duration_in_minutes)
            course.rating = self.get_rating(course.rating)
            courses.append(course)
            print(course.image)
        # courses = [courses[0]]
        if len(courses):
            for i in range(5):
                courses.append(courses[0])
                courses.append(courses[1])

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


class CourseDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        print(pk)
        course = get_object_or_404(Course, pk=pk)
        print(course)
        course_info = get_object_or_404(CourseInfo, course=pk)

        return render(request, 'frontend/course_detail.html', context={
            'course': course,
            'course_info': course_info
        })
