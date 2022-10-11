from rest_framework import serializers
from ...models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер User"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')
        read_only_fields = ('id',)

    username = serializers.CharField(min_length=3, required=True)
    password = serializers.CharField(min_length=8, required=True, write_only=True)
    email = serializers.EmailField(required=True, write_only=True)


    def validate_password(self, value: str) -> str:
        """
        Хэш-значение, переданное пользователем.

         :param value: пароль пользователя
         :return: хешированная версия пароля
        """
        return make_password(value)