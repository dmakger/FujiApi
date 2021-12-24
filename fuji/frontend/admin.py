from django.contrib import admin
from .models import Course, Author, Module, Lesson, Step, Profile

admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Step)
admin.site.register(Profile)
