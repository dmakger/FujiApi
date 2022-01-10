from django.contrib import admin
from .models import Course, Author, Profile


class AuthorAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Profile, ProfileAdmin)
