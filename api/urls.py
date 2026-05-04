# api/urls.py
from django.urls import path
from .views import TaskListAPIView, TaskDetailAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('tasks/', TaskListAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailAPIView.as_view()),
]