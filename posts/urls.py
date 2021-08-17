from django.urls import path
from . import views

urlpatterns = [
    path('post-list/', views.PostListView.as_view(), name='post_list'),
    path('post-detail/<str:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('tags/<str:slug>', views.PostListByTagView.as_view(), name='post_list_by_tag'),
    path('archive/', views.post_archive, name='post_archive'),
]
