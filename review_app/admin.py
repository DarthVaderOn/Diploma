from django.contrib import admin
from review_app.models import Review


# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'post', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('user', 'text', 'post')