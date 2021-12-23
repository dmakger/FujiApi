from django.db import models
from django.contrib.auth.models import User


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
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.URLField()
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
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """
    Урок модуля к курсу
    """
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Step(models.Model):
    """
    Степ к уроку к модулю к курсу
    """
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
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
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avatar_url = models.URLField()
    mail = models.EmailField(max_length=50)
    about_me_text = models.TextField()

    def __str__(self):
        return f'{self.name}_{self.last_name}'


class UserToCourse(models.Model):
    """
    Пользователь к курсу. Какие курсы проходит пользователь
    """
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    progress_points = models.IntegerField()


class UserToModule(models.Model):
    """
    Пользователь к Модулю. Какой модуль в курсе проходит пользователь
    """
    module_id = models.ForeignKey(Module, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class UserToLesson(models.Model):
    """
    Пользователь к Уроку. Какой урок в курсе проходит пользователь
    """
    lesson_id = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)


class UserToStep(models.Model):
    """
    Пользователь к Степу. Какой степ в курсе проходит пользователь
    """
    step_id = models.ForeignKey(Step, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
