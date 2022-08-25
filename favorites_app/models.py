from user_app.models import User
from django.db import models


# Create your models here.


class FriendshipRequest(models.Model):
    """Модель дружбы"""
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='friendship_request')
    user_invite = models.ForeignKey(User,on_delete=models.CASCADE, related_name='friendship')
    friendship_result = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Информационная строка кто с кем дружит"""
        return f"User #{self.user_id} and user #{self.user_invite_id} friendship requested: {self.friendship_result}"


    class Meta:
        """Создаём уникальные поля"""
        unique_together = (('user', 'user_invite'),)


class FollowRequest(models.Model):
    """Модель подписки"""
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='follow_request')
    user_follow = models.ForeignKey(User,on_delete=models.CASCADE, related_name='follow')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Информационная строка кто на кого подписан"""
        return f"User #{self.user_id} follows #{self.user_follow_id}"


    class Meta:
        """Создаём уникальные поля"""
        unique_together = (('user', 'user_follow'),)