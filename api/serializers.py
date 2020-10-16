from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from .models import Post, Comment, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    """Class PostSerializer for Post"""

    author = SlugRelatedField(slug_field='username',
                              read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Class CommentSerializer for Comment"""

    author = SlugRelatedField(slug_field='username',
                              read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Class FollowSerializer for Follow"""

    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(),
        slug_field='username'
    )
    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]


class GroupSerializer(serializers.ModelSerializer):
    """Class GroupSerializer for Group"""

    class Meta:
        fields = '__all__'
        model = Group
