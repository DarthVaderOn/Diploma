from rest_framework import routers
from .favorites import FavoriteProductViewSet


api_router = routers.DefaultRouter()
api_router.register('favorites_product', FavoriteProductViewSet)