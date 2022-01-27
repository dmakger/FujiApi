from django.contrib import admin
from .models import Course, Author, Module, Lesson, Step, \
    CourseInfo, CourseFit, CourseSkill, CourseStars, CourseComment
    # Profile


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
# admin.site.register(Profile)
