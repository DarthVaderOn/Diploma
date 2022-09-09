from rest_framework import serializers
from media_app.api.serializers.media import MediaFileSerializer
from profile_app.api.serializers.profile import UserSerializer
from catalog_app.models import Post


class CatalogSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер постов"""
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ('id', 'user', 'is_public')
        extra_kwargs = {
            'file': {
                    'required': True,
                    'write_only': True,
                    'help_text': 'ID медиа файла',
                },
            }


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


    # media = serializers.URLField(source='file.file.url', read_only=True)
    # media_uploaded_at = serializers.DateTimeField(source='file.uploaded_at', allow_null=True, read_only=True)
    media = MediaFileSerializer(source='file', allow_null=False, read_only=True)
    user = UserSerializer(read_only=True)