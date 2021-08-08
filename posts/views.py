from django.shortcuts import render
from django.views.generic import TemplateView


class PostListView(TemplateView):
    template_name = 'posts/post_list.html'


class PostDetailView(TemplateView):
    template_name = 'posts/post_detail.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class HomeView(TemplateView):
    template_name = 'home.html'
