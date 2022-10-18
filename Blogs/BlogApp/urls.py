from django.urls import path
from . import views

urlpatterns = [
    path('posts', views.posts_create, name="posts_create"),
    path('posts/<str:pk>/', views.posts_update, name="posts_update"),
    path('filter_posts_author/<str:pk>/', views.filter_posts_author, name="filter_posts_author"),
    path('filter_posts_genre/<str:pk>/', views.filter_posts_genre, name="filter_posts_genre"),
    path('filter_posts_between_dates/<str:start>/<str:end>/', views.filter_posts_between_dates, name="filter_posts_between_dates"),
    path('description_length/<int:pk>/', views.description_length, name="description_length"),
]