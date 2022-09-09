from rest_framework import routers
from .category import TagViewSet


api_router = routers.DefaultRouter()
api_router.register('category', TagViewSet)