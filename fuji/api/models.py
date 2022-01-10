from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    """
    Автор курса
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    """
    Курс
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField()
    duration_in_minutes = models.IntegerField()
    rating = models.FloatField(default=0)
    members_amount = models.IntegerField(default=0)
    has_certificate = models.BooleanField()
    max_progress_points = models.IntegerField()

    def __str__(self):
        return self.title


class Module(models.Model):
    """
    Модуль курса
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Урок модуля к курсу
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Step(models.Model):
    """
    Степ к уроку к модулю к курсу
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    """
    Пользователь
    """
    # Расширение класса User (login, password, first_name, last_name)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.ImageField(default="http://localhost:8000/media/logo-person.jpg")
    about_me_text = models.TextField(blank=True, default="")

    def __str__(self):
        return f'{self.pk}'


class UserToCourse(models.Model):
    """
    Пользователь к курсу. Какие курсы проходит пользователь
    """
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    progress_points = models.IntegerField()


class UserToModule(models.Model):
    """
    Пользователь к Модулю. Какой модуль в курсе проходит пользователь
    """
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


class UserToLesson(models.Model):
    """
    Пользователь к Уроку. Какой урок в курсе проходит пользователь
    """
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)


class UserToStep(models.Model):
    """
    Пользователь к Степу. Какой степ в курсе проходит пользователь
    """
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
