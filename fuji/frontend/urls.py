from django.urls import path, re_path

from .views import MainView, CourseView, CourseDetailView
from .views import SignUpView, SignInView
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView


favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('sign-in/', SignInView.as_view(), name='signin'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('course/', CourseView.as_view(), name='course'),
    path('course/<pk>/', CourseDetailView.as_view(), name='course_detail'),
    re_path(r'^favicon\.ico$', favicon_view),
]
