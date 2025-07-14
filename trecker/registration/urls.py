from django.urls import path
from .views import RegistrationView, AuthorizationView


urlpatterns = [
    path("registration/", RegistrationView.as_view(), name = "registration"),
    path("authorization/", AuthorizationView.as_view(), name = "authorization")
]