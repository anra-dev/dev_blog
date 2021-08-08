from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='ex_post_list'),
    path('blog-post/', views.PostDetailView.as_view(), name='ex_post_detail'),
    path('about/', views.AboutView.as_view(), name='ex_about'),
]
