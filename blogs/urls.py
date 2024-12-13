from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    CategoryListView,
    TagListView,
    CommentListView,
    CommentDetailView,
    ProfileDetailView,
    UserRegistrationView,
    UserLoginView,
)

urlpatterns = [
    # Blog Post URLs
    path('blogs/', BlogPostListView.as_view(), name='blogpost_list'),  # To list all blog posts
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost_detail'),  # To get, edit, or delete a specific blog post


]
