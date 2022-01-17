from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, RegisterView, UserView, ProfileView

router = DefaultRouter()
router.register('course', CourseViewSet, basename='course')

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterView.as_view()),
    path("user/", UserView.as_view()),
    path("profile/", ProfileView.as_view()),
]
