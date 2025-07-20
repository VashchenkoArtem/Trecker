from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AboutMeView(TemplateView):
    template_name = "about_me/about_me.html"