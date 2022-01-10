from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "username",
            'id': "input-username",
            'placeholder': "Логин",
        })
    )

    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "password",
            'id': "input-password",
            'placeholder': "Не менее 8 символов",
        })
    )

    repassword = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "repassword",
            'id': "input-repassword",
            'placeholder': "Не менее 8 символов",
        })
    )

    name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "name",
            'id': "input-name",
            'placeholder': "Имя",
        })
    )

    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "last_name",
            'id': "input-last_name",
            'placeholder': "Фамилия",
        })
    )

    mail = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "mail",
            'id': "input-mail",
            'placeholder': "vitalich@yandex.ru",
        })
    )

    def clean(self):
        """Если пароли не совпали очищаем поля и выкидываем исключение"""
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']

        if password != repassword:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        """Сохраняем в бд пользователя. Т.е регистрируем его"""
        User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        ).save()
        return authenticate(**self.cleaned_data)


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "username",
            'id': "input-username",
            'placeholder': "Логин",
        })
    )

    password = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "password",
            'id': "input-password",
            'placeholder': "Пароль",
        })
    )
