from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('create_post/', views.PostCreate.as_view(), name='post_create'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
]
