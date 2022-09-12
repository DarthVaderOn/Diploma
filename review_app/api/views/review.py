from rest_framework import filters, permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.review import ReviewSerializer
from ...models import Review


# CRUD


class ReviewViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, DestroyModelMixin):
    """Создаём класс вьюсет отзывов"""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_field = ['id']
    search_fields = ['=id', 'text', 'user__username']                        # поиск в API
    permission_classes = [permissions.IsAuthenticated]                       # просмотр записей только для авторизованного пользователя