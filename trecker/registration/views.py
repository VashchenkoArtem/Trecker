from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomRegistrationForm, CustomAuthorizationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.


class RegistrationView(CreateView):
    form_class = CustomRegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("authorization")
    
class AuthorizationView(LoginView):
    template_name = "authorization/authorization.html"
    form_class = CustomAuthorizationForm