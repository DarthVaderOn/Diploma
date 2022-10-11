from django.contrib import admin
from favorites_app.models import FavoriteProduct


# Register your models here.


@admin.register(FavoriteProduct)
class FavoriteProductAdmin(admin.ModelAdmin):
    """Вывод полей избранных товаров и настойки админки"""
    list_display = ('user', 'favorite_product', 'created_at')
    list_display_links = ('user', )
    list_filter = ('user',)
    search_fields = ('user__username', 'favorite_product__id')
    readonly_fields = ('created_at',)
    list_editable = ('favorite_product',)