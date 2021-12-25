from django.urls import path

from .views import MainView, CourseView, SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    # path('sign-in/', SignInView.as_view(), name='signin'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('course/', CourseView.as_view(), name='course')
]
