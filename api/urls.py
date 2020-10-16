from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CommentViewSet, PostViewSet,
    FollowViewSet, GroupViewSet
)


v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet)
v1_router.register(r'posts/(?P<post_id>[0-9]+)/comments',
                   CommentViewSet, basename='CommentViewSet')

v1_router.register('follow', FollowViewSet)
v1_router.register('group', GroupViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
