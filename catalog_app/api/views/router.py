from rest_framework import routers
from .catalog import CatalogViewSet


api_router = routers.DefaultRouter()
api_router.register('catalog', CatalogViewSet)