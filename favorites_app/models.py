from catalog_app.models import Post
from user_app.models import User
from django.db import models


# Create your models here.


class FavoriteProduct(models.Model):
    """Модель добавления товаров в избранное"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites_request')
    favorite_product = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Информационная строка какой товар пользователь добавил в избранное"""
        return f"User #{self.user_id} add favorite product #{self.favorite_product_id}"


    class Meta:
        """Создаём уникальные поля"""
        unique_together = (('user', 'favorite_product'),)