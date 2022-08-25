from profile_app.models import Profile
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from profile_app.api.serializers.user import ProfileSerializer
from rest_framework import filters, permissions

from user_app.models import User


class ProfileView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет профиля"""
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    permission_classes = [permissions.IsAuthenticated]                       # просмотр пользователей только для авторизованного пользователя
    search_fields = ['username',]