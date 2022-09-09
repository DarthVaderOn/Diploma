from rest_framework import serializers
from media_app.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер медиафайлов"""
    class Meta:
        model = MediaFile
        fields = '__all__'
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )