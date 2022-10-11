from rest_framework import permissions
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from user_app.api.serializers.users import UserSerializer
from ...models import User


class UserViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    """Создаем класс вьюсет User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]