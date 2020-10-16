from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, Comment, Follow, Group
from .serializers import (
    CommentSerializer, PostSerializer,
    FollowSerializer, GroupSerializer
)
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """ViewSets for Post.
    overridden 'perform_create' method."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        """create method"""

        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSets for Comment.
    overridden 'get_queryset', 'perform_create method'."""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        """Get all comments"""

        post = get_object_or_404(
            Post, pk=self.kwargs.get("post_id")
        )
        return post.comments.all()

    def perform_create(self, serializer):
        """create method"""

        serializer.save(author=self.request.user)


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSets for Follow.
        overridden 'perform_create' method."""

    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username' ]

    def perform_create(self, serializer):
        """create method"""

        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """ViewSets for Group"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
