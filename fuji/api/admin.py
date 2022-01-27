from django.contrib import admin
from .models import Profile, Author, Course, Module, Lesson, Step, \
    CourseInfo, CourseFit, CourseSkill, CourseStars, CourseComment


class AuthorAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Step)

admin.site.register(CourseInfo)
admin.site.register(CourseFit)
admin.site.register(CourseSkill)
admin.site.register(CourseStars)
admin.site.register(CourseComment)
admin.site.register(Profile)
