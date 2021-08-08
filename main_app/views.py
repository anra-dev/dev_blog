from django.shortcuts import render
from django.views.generic import TemplateView


class PostListView(TemplateView):
    template_name = 'main_app/post_list.html'


class PostDetailView(TemplateView):
    template_name = 'main_app/post_detail.html'


class AboutView(TemplateView):
    template_name = 'main_app/about.html'
