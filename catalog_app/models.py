from django.db import models
from category_app.models import Tag
from media_app.models import MediaFile
from user_app.models import User


# Create your models here.


class Post(models.Model):
    """Модель товаров"""
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='catalogs', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT, verbose_name='Tags')
    file = models.ForeignKey(MediaFile, on_delete=models.SET_NULL, null=True, blank=True)
    year = models.PositiveIntegerField("Year", default=2022)
    country = models.CharField("Country", max_length=10)
    price = models.PositiveIntegerField("Price", default=0, help_text="Indicate the amount in Belarusian rubles")


class Media(models.Model):
    """Модель изображений товаров"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="media_post")
    image_post = models.ImageField(null=False, blank=True)