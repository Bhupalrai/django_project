from django.contrib import admin
from django.urls import path

from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    #class based view needs certain naming convention
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]
