from rest_framework import filters, permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.catalog import CatalogSerializer
from catalog_app.models import Post


# CRUD
class CatalogViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    """Создаём класс вьюсет каталога"""
    serializer_class = CatalogSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_field = ['created_at', 'id']
    search_fields = ['=id', 'title', 'text', 'user__username']               # поиск в API
    permission_classes = [permissions.IsAuthenticated]                       # просмотр записей только для авторизованного пользователя


    def perform_destroy(self, instance):
        instance.is_public = False
        instance.save()