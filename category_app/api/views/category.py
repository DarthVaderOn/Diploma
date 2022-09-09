from rest_framework import filters, permissions
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.category import TagSerializer
from category_app.models import Tag


class TagViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет тегов"""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    filter_backends = [filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]                       # просмотр тегов только для авторизованного пользователя
    ordering_fields = '__all__'