from rest_framework import serializers
from category_app.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Создаем класс сериалайзер тегов"""
    class Meta:
        model = Tag
        fields = '__all__'                          # вывод всех полей