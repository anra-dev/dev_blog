from django.shortcuts import render
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'main_app/index.html'


class BlogPostView(TemplateView):
    template_name = 'main_app/blog-post.html'


class AboutView(TemplateView):
    template_name = 'main_app/about.html'
