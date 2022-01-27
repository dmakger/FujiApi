# from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404
from django.urls import path
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, pagination

from .serializers import CourseSerializer, CourseInfoSerializer
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer

from .models import Course, Profile, CourseInfo


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = 'created_at'


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseSerializer
        elif self.action == 'retrieve':
            return CourseInfoSerializer

    def retrieve(self, request, pk=None, *args, **kwargs):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        course_info = serializer.get_info(pk)
        return Response({
            "course": serializer.data,
            "info": course_info
        })


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'message': "Пользователь успешно создан"
        })


class UserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })
