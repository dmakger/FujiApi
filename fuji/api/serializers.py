from rest_framework import serializers
from .models import Author, Course, Profile
from django.contrib.auth.models import User


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())

    class Meta:
        model = Course
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 're_password', 'first_name', 'last_name', 'email')
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        re_password = validated_data['re_password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']

        if password != re_password:
            raise serializers.ValidationError({'password': "Пароли не совпадают"})

        user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        user.set_password(password)
        user.save()
        profile = Profile(user=user)
        profile.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
