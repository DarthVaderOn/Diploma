from rest_framework import routers
from .review import ReviewViewSet


api_router = routers.DefaultRouter()
api_router.register('review', ReviewViewSet)