# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, generics, pagination

from .serializers import CourseSerializer
from .serializers import RegisterSerializer, UserSerializer, ProfileSerializer

from .models import Course, Profile


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    ordering = 'created_at'


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(user, context=self.get_serializer_context()).data
        profile = Profile.objects.get(user=user_data['id'])
        profile_data = ProfileSerializer(profile, context=self.get_serializer_context()).data
        return Response({
            'user': user_data,
            'profile': profile_data,
            'message': "Пользователь успешно создан"
        })


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            "profile": ProfileSerializer(request.user.profile, context=self.get_serializer_context()).data
        })


class UserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data
        })
