from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomRegistrationForm
from django.urls import reverse_lazy
# Create your views here.

class RegistrationView(CreateView):
    form_class = CustomRegistrationForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        user = form.save()
        user.username = f"user-{user.pk}"
        user.save()
        return super().form_valid(form)
    