from django.db import models
from catalog_app.models import Post
from user_app.models import User


# Create your models here.


class Review(models.Model):
    """Модель комментариев"""
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='comments')