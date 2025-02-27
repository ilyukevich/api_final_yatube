from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    """creating a GROUP model"""

    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique=True, null=True)
    description = models.TextField('description', null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    """creating a POST model"""

    text = models.TextField()
    pub_date = models.DateTimeField(
        "Дата публикации", auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="posts"
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="posts"
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    """creating a Comment model"""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="comments"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comments"
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True, db_index=True
    )


class Follow(models.Model):
    """creating a Follow model"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        unique_together = ('user', 'following')
