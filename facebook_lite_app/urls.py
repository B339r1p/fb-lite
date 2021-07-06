from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import PostViewSet,CommentViewSet,LikeViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'like', LikeViewSet)

urlpatterns = [
    path("", include(router.urls))
]