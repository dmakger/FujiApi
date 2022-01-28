from rest_framework import serializers
from .models import Author, Course, Profile
from .models import CourseInfo, CourseFit, CourseSkill, CourseStars, CourseComment
from django.contrib.auth.models import User


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_profile(self, user):
        return ProfileSerializer(user.profile).data


class CourseSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="name", queryset=Author.objects.all())

    class Meta:
        model = Course
        fields = '__all__'

    def get_info(self, pk):
        queryset = CourseInfo.objects.get(course_id=pk)
        return CourseInfoSerializer(queryset).data


class CourseInfoSerializer(serializers.ModelSerializer):
    fit = serializers.SerializerMethodField()
    skill = serializers.SerializerMethodField()
    stars = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = CourseInfo
        fields = ['title_image', 'goal_description', 'fit', 'skill', 'stars', 'comments']

    def get_fit(self, course_info):
        queryset = CourseFit.objects.filter(course_info_id=course_info.pk)
        return CourseFitSerializer(queryset, many=True).data

    def get_skill(self, course_info):
        queryset = CourseSkill.objects.filter(course_info_id=course_info.pk)
        return CourseSkillSerializer(queryset, many=True).data

    def get_stars(self, course_info):
        queryset = CourseStars.objects.get(course_info_id=course_info.pk)
        return CourseStarsSerializer(queryset).data

    def get_comments(self, course_info):
        queryset = CourseComment.objects.filter(course_info_id=course_info.pk)
        return CourseCommentSerializer(queryset, many=True).data


class CourseFitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseFit
        fields = ['title', 'description']
        # fields = '__all__'


class CourseSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSkill
        fields = ['name']


class CourseStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseStars
        fields = ['five_stars_count', 'four_stars_count', 'three_stars_count', 'two_stars_count', 'one_stars_count']


class CourseCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = CourseComment
        fields = ['user', 'created_at', 'comment', 'stars_count']

    def get_user(self, course_info):
        user = User.objects.get(pk=course_info.pk)
        return UserCommentSerializer(user).data


class UserCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']