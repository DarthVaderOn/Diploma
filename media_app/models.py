from user_app.models import User
from django.db import models


# Create your models here.


class MediaFile(models.Model):
    """Модель медиафайлов"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    file = models.ImageField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)