from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    first_name = forms.CharField(max_length = 256, label = "Ім'я")
    last_name = forms.CharField(max_length = 256, label = "Прізвище")
    email = forms.EmailField(max_length = 512, label = "Пошта")
    password1 = forms.CharField(max_length = 12, widget = forms.PasswordInput, label = "Пароль")
    password2 = forms.CharField(max_length = 12, widget = forms.PasswordInput, label = "Підтвердження пароля")