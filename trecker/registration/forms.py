from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from collections import OrderedDict


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    username = forms.CharField(max_length = 256, label = "Ім'я")
    email = forms.EmailField(max_length = 512, label = "Пошта")
    password1 = forms.CharField(max_length = 12, widget = forms.PasswordInput, label = "Пароль")
    password2 = forms.CharField(max_length = 12, widget = forms.PasswordInput, label = "Підтвердження пароля")

class CustomAuthorizationForm(AuthenticationForm):
    username = forms.CharField(max_length=256, label="Ім'я")
    email = forms.EmailField(max_length=512, label="Пошта")
    password = forms.CharField(max_length=12, widget=forms.PasswordInput, label="Пароль")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = OrderedDict([
            ('username', self.fields['username']),
            ('email', self.fields['email']),
            ('password', self.fields['password']),
        ])