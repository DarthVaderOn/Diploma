from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.favorites import FavoriteProductSerializer
from ...models import FavoriteProduct


class FavoriteProductViewSet(GenericViewSet, ListModelMixin, CreateModelMixin):
    """Создаём класс вьюсет избранные товары"""
    serializer_class = FavoriteProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = FavoriteProduct.objects.all()