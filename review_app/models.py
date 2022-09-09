from django.db import models
from catalog_app.models import Post
from user_app.models import User


# Create your models here.


class Review(models.Model):
    """Модель отзывов"""
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=False, null=False, max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='reviews')


class MediaReview(models.Model):
    """Модель изображений отзывов"""
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="image")
    image_review = models.ImageField(null=False, blank=True)