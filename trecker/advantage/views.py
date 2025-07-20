from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class AdvantagesView(TemplateView):
    template_name = "advantage/advantage.html"