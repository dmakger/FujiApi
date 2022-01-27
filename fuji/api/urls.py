from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
# router.register('courset', CourseViewSet, basename='courset')

urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.RegisterView.as_view()),
    path("user/", views.UserView.as_view()),
    path("course/", views.CourseViewSet.as_view({'get': 'list'})),
    path("course/<int:pk>", views.CourseViewSet.as_view({'get': 'retrieve'})),
]