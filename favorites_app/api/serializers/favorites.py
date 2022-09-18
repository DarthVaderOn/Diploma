from rest_framework import serializers
from favorites_app.models import FavoriteProduct


class FavoriteProductSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер избранные товары"""
    class Meta:
        model = FavoriteProduct
        fields = '__all__'
        read_only_fields = ['user']


    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )