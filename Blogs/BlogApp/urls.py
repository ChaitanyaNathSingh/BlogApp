from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.posts_create, name="posts_create"),
    path('posts/<str:title>/', views.posts_update, name="posts_update")
]