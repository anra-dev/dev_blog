from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('post-list/', views.PostListView.as_view(), name='post_list'),
    path('post-detail/', views.PostDetailView.as_view(), name='post_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
]
