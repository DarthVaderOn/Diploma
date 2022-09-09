from rest_framework import routers
from .media import MediaFileViewSet


api_router = routers.DefaultRouter()
api_router.register('media', MediaFileViewSet)