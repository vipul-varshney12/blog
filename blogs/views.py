from rest_framework import generics, permissions
from .models import BlogPost, Comment, Category, Tag
from .serializers import BlogPostSerializer, CommentSerializer, CategorySerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated

# BlogPost Views
class BlogPostListView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all().order_by('-created_at')  # Order by most recent first
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated users to view

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)  # Save creator as the currently logged in user

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]  # Only logged in users can modify or delete

# Comment Views
class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Only logged in users can comment

    def get_queryset(self):
        blogpost_id = self.kwargs['blogpost_id']
        return Comment.objects.filter(post__id=blogpost_id)

    def perform_create(self, serializer):
        blogpost_id = self.kwargs['blogpost_id']
        serializer.save(user=self.request.user, post_id=blogpost_id)  # Save user and post ID

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Only logged in users can modify or delete

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)  # Ensure user can only access their comments

# Category Views
class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated users to view

# Tag Views
class TagListView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]  # Allow unauthenticated users to view
