from rest_framework import permissions
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from media_app.api.serializers.media import MediaFileSerializer
from media_app.models import MediaFile


class MediaFileViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    """Создаём класс вьюсет медиафайлов"""
    serializer_class = MediaFileSerializer
    permission_classes = [permissions.IsAuthenticated]                       # просмотр медиафайлов только для авторизованного пользователя
    queryset = MediaFile.objects.all()