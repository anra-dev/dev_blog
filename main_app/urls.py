from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main-page'),
    path('blog-post/', views.BlogPostView.as_view(), name='blog-post'),
    path('about/', views.AboutView.as_view(), name='about'),
]