from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'main_app/home.html'


class AboutView(TemplateView):
    template_name = 'main_app/about.html'

