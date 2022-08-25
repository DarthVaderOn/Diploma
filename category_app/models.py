from django.db import models


# Create your models here.


class Tag(models.Model):
    """Модель категорий"""
    title = models.CharField(max_length=64, null=True, blank=True, unique=True, verbose_name='Tag')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tag'
