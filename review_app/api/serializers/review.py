from rest_framework import serializers
from media_app.api.serializers.media import MediaFileSerializer
from profile_app.api.serializers.profile import UserSerializer
from review_app.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер отзывов"""
    class Meta:
        model = Review
        exclude = ['created_at']
        read_only_fields = ('id', 'user',)
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


    media = MediaFileSerializer(source='file', allow_null=False, read_only=True)
    user = UserSerializer(read_only=True)