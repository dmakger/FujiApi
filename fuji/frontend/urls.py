from django.urls import path

from .views import MainView, CourseView

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('course/', CourseView.as_view(), name='course')
]
